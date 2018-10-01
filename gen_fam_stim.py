#!/usr/bin/env python3

class Stim:
    ''' A stimulus '''
    def __init__(self, step=0, speaker=0):
        self.step = int(step)
        self.speaker = int(speaker)
        if self.step < 1 or self.step > 8:
            raise ValueError(
                "step = {}: valid range for step = 1 <= step <= 8".format(step)
                )
        
        if self.speaker < 1 or self.speaker > 4:
            raise ValueError(
                "speaker = {}valid range for speaker 1 <= speaker <= 4".format(
                    speaker
                    )
                )

    def __str__(self):
        return "ae_{}_0{}".format(self.step, self.speaker)


class StimGenerator:
    ''' Generates a list of stimuli '''

    def __init__(self, steps, speakers):
        self.stims = [Stim(step,speak) for step, speak in zip(steps, speakers)]

    def create_str_list(self):
        return [str(i) for i in self.stims]

def create_dist_from_hist(l):
    ''' Create a distribution from a histogram '''
    lout = []
    for i in range(len(l)):
        lout += ([i+1] *l[i])
    return lout

def create_hist_from_dist(l):
    d = {}
    output = ""
    for i in l:
        try:
            d[i] += 1
        except KeyError:
            d[i] = 1
    for key in sorted(d.keys()):
        output += "{}\t{}\n".format(key, "*" * d[key])
    return output

def zep_strarr_format(name, strlist, indent="    "):
    ''' Prints a zep string array constant '''
    string = "string[..] {} = {}\n".format(name, "{")
    for i in strlist:
        string += "{}\"{}\",\n".format(indent, i)
    string += "};"
    return string


bi_hist     = [8, 36, 16, 8, 8, 16, 36, 8]
uni_hist    = [8, 8, 16, 36, 36, 16, 8, 8]
assert(len(bi_hist) // 4 == len(bi_hist) / 4)
assert(sum(bi_hist) // 4 == sum(bi_hist) / 4)
assert(len(uni_hist) // 4 == len(uni_hist) / 4)
assert(sum(uni_hist) // 4 == sum(uni_hist) / 4)
assert(sum(uni_hist) == sum(bi_hist))
assert(len(uni_hist) == len(bi_hist))

speaker_list= [1, 2, 3, 4] * (sum(bi_hist) // 4)
assert(len(speaker_list) == sum(bi_hist))

print ("sum_bidist = {}".format(sum(bi_hist)) )
print ("sum_unidist = {}".format(sum(uni_hist)) )

uni_dist = create_dist_from_hist(uni_hist)
bi_dist  = create_dist_from_hist(bi_hist)

uni_gen  = StimGenerator(uni_dist, speaker_list)
bi_gen   = StimGenerator(bi_dist, speaker_list)

uni_list = uni_gen.create_str_list()
bi_list  = bi_gen.create_str_list()

zep_bi_ouput    = zep_strarr_format("bimodal", bi_list)
zep_uni_ouput   = zep_strarr_format("unimodal", uni_list)

print (zep_bi_ouput)
print(create_hist_from_dist(bi_list))
print (zep_uni_ouput)
print(create_hist_from_dist(uni_list))

