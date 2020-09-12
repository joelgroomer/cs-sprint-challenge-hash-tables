#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = []
    trips = {}
    for ticket in tickets:
        trips[ticket.source] = ticket.destination

    print(trips)
    start = 'NONE'
    while True:
        val = trips[start]
        route.append(val)
        start = val
        if start == 'NONE':
            break

    return route
