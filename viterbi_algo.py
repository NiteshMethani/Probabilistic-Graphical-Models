def viterbi(obs, states, start_p, trans_p, emit_p):

    V = [{}]

    for st in states:

        V[0][st] = {"prob": start_p[st] * emit_p[st][obs[0]], "prev": None}

    # Run Viterbi when t > 0

    for t in range(1, len(obs)):

        V.append({})

        for st in states:

            max_tr_prob = max(V[t-1][prev_st]["prob"]*trans_p[prev_st][st] for prev_st in states)

            for prev_st in states:

                if V[t-1][prev_st]["prob"] * trans_p[prev_st][st] == max_tr_prob:

                    max_prob = max_tr_prob * emit_p[st][obs[t]]

                    V[t][st] = {"prob": max_prob, "prev": prev_st}

                    break

    for line in dptable(V):

        print line
    print("*************************************************")
    opt = []

    # The highest probability

    max_prob = max(value["prob"] for value in V[-1].values())

    previous = None

    # Get most probable state and its backtrack

    for st, data in V[-1].items():

        if data["prob"] == max_prob:

            opt.append(st)

            previous = st

            break

    # Follow the backtrack till the first observation

    for t in range(len(V) - 2, -1, -1):

        opt.insert(0, V[t + 1][previous]["prev"])

        previous = V[t + 1][previous]["prev"]


    print 'The steps of states are ' + ' '.join(opt) + ' with highest probability of %s' % max_prob


def dptable(V):

    # Print a table of steps from dictionary

    yield " ".join(("%12d" % i) for i in range(len(V)))

    for state in V[0]:

        yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)


# obs = ('normal', 'cold', 'dizzy')
# states = ('Healthy', 'Fever')
# start_p = {'Healthy': 0.6, 'Fever': 0.4}
# trans_p = {
#    'Healthy' : {'Healthy': 0.7, 'Fever': 0.3},
#    'Fever' : {'Healthy': 0.4, 'Fever': 0.6}
#    }
# emit_p = {
#    'Healthy' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
#    'Fever' : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
#    }


obs = ('A', 'B', 'B', 'D', 'C')
states = ('state_A', 'state_B', 'state_C', 'state_D')
start_p = {'state_A':0.25, 'state_B':0.25, 'state_C':0.25, 'state_D':0.25}
trans_p = {
   'state_A' : {'state_A': 0.5, 'state_B': 0.25, 'state_C': 0, 'state_D': 0.25},
   'state_B' : {'state_A': 0.25, 'state_B': 0.5, 'state_C': 0.25, 'state_D': 0},
   'state_C' : {'state_A': 0, 'state_B': 0.25, 'state_C': 0.5, 'state_D': 0.25},
   'state_D' : {'state_A': 0.25, 'state_B': 0, 'state_C': 0.25, 'state_D': 0.5}
   }
emit_p = {
   'state_A' : {'A': 0.5, 'B': 0.5/3, 'C': 0.5/3, 'D': 0.5/3},
   'state_B' : {'A': 0.5/3, 'B': 0.5, 'C': 0.5/3, 'D': 0.5/3},
   'state_C' : {'A': 0.5/3, 'B': 0.5/3, 'C': 0.5, 'D': 0.5/3},
   'state_D' : {'A': 0.5/3, 'B': 0.5/3, 'C': 0.5/3, 'D': 0.5}
   }



viterbi(obs,
                   states,
                   start_p,
                   trans_p,
                   emit_p)
