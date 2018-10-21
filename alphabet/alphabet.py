import struct
import wallaroo


class Votes(object):
    def __init__(self, letter, votes):
        self.letter = letter
        self.votes = votes;


class AllVotes(object):
    def __init__(self):
        self.votes_by_letter = {}

    def update(self, votes):
        letter = votes.letter
        vote_count = votes.votes
        votes_for_letter = self.votes_by_letter.get(letter, Votes(letter, 0))
        votes_for_letter.votes += vote_count
        self.votes_by_letter[letter] = votes_for_letter

    def get_votes(self, letter):
        vbl = self.votes_by_letter[letter]
        # Return a new Votes instance here!
        return Votes(letter, vbl.votes)


@wallaroo.decoder(header_length=4, length_fmt='>I')
def decoder(bs):
    (letter, vote_count) = struct.unpack(">sI", bs)
    return Votes(letter, vote_count)

@wallaroo.encoder
def encoder(data):
    return "%s => %d\n" % (data.letter, data.votes)


@wallaroo.state_computation(name="add votes")
def add_votes(data, state):
    state.update(data)
    return (state.get_votes(data.letter), True)


def application_setup(args):
    in_host, in_port = wallaroo.tcp_parse_input_addrs(args)[0]
    out_host, out_port = wallaroo.tcp_parse_output_addrs(args)[0]

    ab = wallaroo.ApplicationBuilder("alphabet")
    ab.new_pipeline("alphabet",
                    wallaroo.TCPSourceConfig(in_host, in_port, decoder))
    ab.to_stateful(add_votes, AllVotes, "letter state")
    ab.to_sink(wallaroo.TCPSinkConfig(out_host, out_port, encoder))
    return ab.build()
    