import random
import matplotlib.pyplot as plt

exp_num = 30
city = []
g_rows = []
infection_spread = []
inf_house_list = set()
num_column = 10
num_row = 10


class House:
    def __init__(self, housenum, x_coord, y_coord, num_people, residentlist, inf_count, inf_list, neighbours, neighlist, state):
        self.id = housenum
        self.row = x_coord
        self.col = y_coord
        self.people = num_people
        self.reslist = residentlist
        self.infcount = inf_count
        self.inflist = inf_list
        self.neigh = neighbours
        self.neighlist = neighlist
        self.state = state

    def __str__(self):
        return 'House(id =' + str(self.id) + ', row =' + str(self.row) + ' col =' + str(self.col) + ' people =' + \
               str(self.people) + ', residentlist =' + str(self.reslist) + ', infcount =' + str(self.infcount) +', inf list =' + str(self.inflist) +\
               ' neighbours =' + str(self.neigh) + ' neighbour list =' + str(self.neighlist) + ', state =' + str(self.state) + ')'


class Person:
    def __init__(self, personnum, house, state, trans_prob, inf_prob):
        self.id = personnum
        self.inhouse = house
        self.state = state
        self.trans = trans_prob
        self.infect = inf_prob

    def __str__(self):
        return 'Person(id = ' + str(self.id) + ', house = ' + str(self.inhouse) + ', state = ' + str(self.state) + ', transmission rate = ' + str(self.trans) + ', infection rate = ' + str(self.infect) + ')'


def fillrow(start_num):
    rows = []
    j = start_num
    for i in range(num_column):
        j = j+1
        rows.append(j)
    return j, rows


def fill_city ():
    temp_no = 0
    temp_end = 0
    for  houseno in range(num_row):
        temp_no, g_rows = fillrow(temp_no)
        #print("temp no:", temp_no , "row:", g_rows)
        city.append(g_rows)


print("City", city)


def get_house_no(x, y):
    return (city[x][y])


def set_house_no(x, y, houseno):
   city[x][y] = houseno
   return city[x][y]


#print( "City", city)
#houseno = get_house_no(1, 0)
#print("houseno", houseno)

# houseno = set_house_no(1, 0, 47)
# houseno = get_house_no(1, 0)
# print("new houseno", houseno)
# print("City", city)

house_list = []


def create_house_list():
    for x in range(num_row * num_column):
        h = House(x+1, 0, 0, random.randint(0, 10), 0, 0, 0, 0, 0, random.randint(0, 0))
        #4print("house %",  x+1, h)
        house_list.append(h)

#print("house list: ", house_list)
#user_num = int(input("house number = "))
#h = house_list[user_num]
#print("house %",  user_num, h)
#print("specific house #", house_list[user_num])


def find_house(x, y):
   # print("Enter in find_house", x, y)
    found_house_num = int(city[x][y])
    #print("house number found:", found_house_num)
    h = house_list[found_house_num-1]
    return h


def set_house_cordinates(x, y):
    h = find_house(x, y)
    h.row = x
    h.col = y
    #print("specific house #", h)
    return h


def fill_house_cordinates():
    for x in range(num_row):
        for y in range(num_column):
            h = find_house(x, y)
            #print("house details:", h)
            h = set_house_cordinates(x, y)
            #print("new house details:", h)


def get_neighbours(house_num):
    h = house_list[house_num - 1]
    x = h.row
    y = h.col
    neighbours_list = []

    if (x - 1) >= 0:
        neigh_house_no = get_house_no(x-1, y)
        neighbours_list.append(neigh_house_no)

    if (x + 1) < num_row:
        neigh_house_no = get_house_no(x+1, y)
        neighbours_list.append(neigh_house_no)

    if (y - 1) >= 0:
        neigh_house_no = get_house_no(x, y-1)
        neighbours_list.append(neigh_house_no)

    if (y + 1) < num_column:
        neigh_house_no = get_house_no(x, y+1)
        neighbours_list.append(neigh_house_no)

    if (x - 1) >= 0 and (y + 1) < num_column:
        neigh_house_no = get_house_no(x-1, y+1)
        neighbours_list.append(neigh_house_no)

    if (x - 1) >= 0 and (y - 1) >= 0:
        neigh_house_no = get_house_no(x-1, y-1)
        neighbours_list.append(neigh_house_no)

    if (x + 1) < num_row and (y + 1) < num_column:
        neigh_house_no = get_house_no(x+1, y+1)
        neighbours_list.append(neigh_house_no)

    if (x + 1) < num_row and (y - 1) >= 0:
        neigh_house_no = get_house_no(x+1, y-1)
        neighbours_list.append(neigh_house_no)

    neighbours_list.sort()
    num_neighbours = len(neighbours_list)
    return neighbours_list, num_neighbours



def set_house_neighbours(x, y):
    h = find_house(x, y)
    a, b = get_neighbours(h.id)
    h.neigh = b
    h.neighlist = a
    #print("setting neighbour:", h)
    return h


def fill_neighbours():
    for x in range(num_row):
        for y in range(num_column):
            h = set_house_neighbours(x, y)


def print_classhouse():
    for i in range(num_column*num_row):
        print(house_list[i])


def create_people_plot():
    x = list(range(num_row))
    plt.xlabel('column number')
    plt.ylabel('row number')
    plt.title('population density in city')
    for j in range(num_column):
        y = [j] * num_row
        people_in_house = []
        for i in range(num_row):
            h = find_house(x[i], y[i])
            num_people = h.people
            people_in_house.append(num_people)
        print("number of people in row:", people_in_house)

        for i in range(num_row):
                plt.scatter(x[i], y[i], color="b", s=people_in_house[i]*50)
    # plt.show()
    plt.savefig('test-runs/people_plot_%d.png' % exp_num)

def create_state_plot():
    x = list(range(num_row))
    plt.xlabel('column number')
    plt.ylabel('row number')
    plt.title('infection state in city')
    for j in range(num_column):
        y = [j] * num_row
        state_in_house = []
        for i in range(num_row):
            h = find_house(x[i], y[i])
            state = h.state
            state_in_house.append(state)
        #print("state of people in row:", state_in_house)

        for i in range(num_row):
            if state_in_house[i] == 1:
                plt.scatter(x[i], y[i], color="red", s=1)
            else:
                plt.scatter(x[i], y[i], color="black", s=1 )
    # plt.show()
    plt.savefig('test-runs/state_plot_%d.png' % exp_num)


def create_infection_spread_plot():
    x = list(range(len(infection_spread)))
    y = infection_spread
    plt.xlabel('day')
    plt.ylabel('infected population')
    plt.title('infection spread in city')
    plt.scatter(x, y)
    # plt.show()
    plt.savefig('test-runs/inf_spread_plot_%d.png' % exp_num)


def population_count():
    pop = 0
    for x in range(num_row * num_column):
        h = house_list[x]
        pop = pop + h.people
    return pop


person_list = []


def create_person_list(p0):
    pop = 0
    for x in range(num_column * num_row):
        h = house_list[x]
        people_in_house = []
        people_infected = []
        num_people_infected = 0
        for j in range(h.people):
            p = Person(pop + j, h.id, random.randint(0, 0), 15, 50)
            if p.id == p0: # initialising patient zero
                p.state = 1
            person_list.append(p)
            people_in_house.append(p.id)
            if p.state == 1:
                people_infected.append(p.id)
                num_people_infected = num_people_infected + 1
                h.state = 1
        pop = pop + h.people
        h.reslist = people_in_house
        h.infcount = num_people_infected
        h.inflist = people_infected
    return pop


def print_classperson():
    for i in range(population_count()):
        print(person_list[i])


def move_person_to_specific_house(person_id, house_id):# takes person number, moves person to any given house
    p = person_list[person_id]
    current_house_num = p.inhouse
    h_curr = house_list[current_house_num - 1]
    new_house_num = house_id
    h_next = house_list[new_house_num - 1]

    # updating Person properties
   # print("person before moving:", p)
    p.inhouse = new_house_num
   # print("person after moving:", p)

    # updating House properties

    # updating old house
    #print("current house before moving:", h_curr)
    h_curr.people = h_curr.people - 1
    h_curr.reslist.remove(p.id)
    if p.state == 1:
        # print("person id: ", p.id)
        h_curr.inflist.remove(p.id)
        h_curr.infcount = h_curr.infcount - 1
        if h_curr.infcount == 0:
            h_curr.state = 0
            # inf_house_list.remove(h_curr.id) ### fix how to remove
    # print("current house after moving:", h_curr)

    # updating new house
    # print("next house before moving:", h_next)
    h_next.people += 1
    h_next.reslist.append(p.id)
    h_next.reslist.sort()
    if p.state == 1:
        h_next.inflist.append(p.id)
        h_next.state = 1
        inf_house_list.add(h_next.id)
    h_next.inflist.sort()
    h_next.state = h_next.state or p.state
    print("person ", p)
    print("house: ", h_next)

    # updating people in new house
    if p.state == 1:
        h_next.infcount = h_next.people
        h_next.inflist = []
        # print("h_next.infcount = ", h_next.infcount, " h_next.people = ",  h_next.people)
        for i in range(h_next.infcount):
            person_num = h_next.reslist[i]
            r = person_list[person_num]
            r.state = 1
            h_next.inflist.append(r.id)
            # print("h_next.people = ", h_next.people)
            # print("resident number", r)
            # print("next house details:", h_next)
    # print("next house after moving:", h_next)


def move_person(person_id): # takes person number, moves person to the first neighbour
    p = person_list[person_id]
    current_house_num = p.inhouse
    h_curr = house_list[current_house_num - 1] # House Index is 0 based, House Number is 1 based
   # print("move person h_curr:", h_curr)
    new_house_num = h_curr.neighlist[0]
    move_person_to_specific_house(person_id, new_house_num)


def move_house_members(house_id):  # takes house number, moves every person in house to different neighbours in RR,
    # find all people in house , find all neighbours, move one person to one neighbour
    h_current_house_num = house_id
    h_curr = house_list[h_current_house_num - 1]
    # print("move house members h_curr:", h_curr)
    i = h_curr.people
    while i > 0:
        # print("index no.: ", i)
        r = h_curr.reslist[h_curr.people-1]
        h_new_house_num = h_curr.neighlist[i % h_curr.neigh]
        move_person_to_specific_house(r, h_new_house_num)
        # print("moved person ", r, "from ", h_curr.id, "to ", h_new_house_num)
        # print("new house details: ", house_list[h_new_house_num - 1])
        i = h_curr.people

def infected_count():
    #print("population count from list:", len(person_list))
    pop = len(person_list)
    infected_count = 0
    for i in range(pop):
        p = person_list[i]
        if p.state == 1:
            infected_count = infected_count + 1
    return infected_count


# moving everyone to first neighbour for set number of days


def spread_over_time_p0(num_days):
    for day in range(num_days):
        for i in range(5):  # (len(house_list)):
            move_person(i)
        infected_pop = infected_count()
        infection_spread.append(infected_pop)


# moving everyone in house to different neighbour for set number of days


def spread_over_time_h0(num_days):
    for day in range(num_days):
        #for i in range(len(house_list)):
        p = person_list[p0]
        h = p.inhouse
        move_house_members(h)
        infected_pop = infected_count()
        infection_spread.append(infected_pop)





def spread_through_inf_houses(num_days):
    p = person_list[p0]
    h0 = p.inhouse
    for i in range(0): # (len(house_list)):
        h = house_list[i]
        if h.state == 1:
            move_house_members(h.id)
        infected_pop = infected_count()
        infection_spread.append(infected_pop)


# Main routines

fill_city()
print("City", city)
#houseno = get_house_no(0, 0)
#print("houseno", houseno)

create_house_list()
fill_house_cordinates()

#neighbours, num_neighbours = get_neighbours(2)
#print("number of neighbours:", num_neighbours, "neighbour house numbers :", neighbours)

p0 = 0
fill_neighbours()
total_population = create_person_list(p0)
print("patient 0:", person_list[0])
print("total population = ", total_population)

infected_pop = infected_count()
infection_spread.append(infected_pop)

#create_people_plot()
#create_state_plot()

# moving everyone to next neighbour for set number of days


spread_over_time_p0(30)
#spread_over_time_h0(30)
# spread_through_inf_houses(30)

print("list of infected houses: ", inf_house_list)


#move_person_to_specific_house(7, 8)
infected_pop = infected_count()
infection_spread.append(infected_pop)


# print_classhouse()
# print_classperson()

# infected_pop = infected_count()
print("total population = ", total_population)
print("infected population number:", infected_pop)
print("infection spread:", infection_spread)

create_people_plot()
create_state_plot()
create_infection_spread_plot()

