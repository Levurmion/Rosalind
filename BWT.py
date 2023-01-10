'''
This project is an object-oriented implementation of the Burrows-Wheeler algorithm for DNA sequences.

string: ATTGTGTTCCTCCTAGCTAGCGAGTTTCAGAACCCCGTA
'''

class DNA:

    def __init__(self, sequence):
        self.seq = sequence.upper()

    
    ### function to parse the BWT compression
    def parse(self, BWT_string):

        expanded_BWT = ''
        run_char = ''   # keep track of the last char in case it could be a run
        count_str = ''  # package numbers as strings first because there may be multiple digits

        for char in BWT_string:

            # check if the char is a number (indicates a run for a previous char)
            try:
                count_char = int(char)
                count_str = count_str + char   
            
            # char is not a number, indicates either no runs, or all digits for count_str has been recorded
            except ValueError:

                # no previously detected runs
                if count_str == '':     
                    expanded_BWT = expanded_BWT + char
                    run_char = char
                # a run was previously detected and all digits completely packed into count_str
                elif count_str != '':   
                    count = int(count_str)
                    expanded_BWT = expanded_BWT + run_char*(count-1) + char
                    run_char = char
                    count_str = ''  # reset
        
        # check if the last character was a run
        if count_str != '':
            count = int(count_str)
            expanded_BWT = expanded_BWT + run_char*(count-1)
        
        return expanded_BWT


    ### function to generate the BWT left and right col
    def generate_BWT_cols(self, BWT_string):

        BWT_rightcol = []
        BWT_leftcol = []

        # keep track of which items appended
        BWT_appended = ''                   
        
        for char in BWT_string:
            char_count = BWT_appended.count(char)
            BWT_rightcol.append((str(char_count+1) + char))
            BWT_appended = BWT_appended + char

        BWT_leftcol = list.copy(BWT_rightcol)
        BWT_leftcol.sort(key=lambda x: x[-1])

        return BWT_leftcol, BWT_rightcol


    ### compress method using BWT algorithm
    def compress(self):

        string = '$' + self.seq
        str_len = len(string)

        BWT_perm = []  # save all cyclic permutation

        for i in range(0,str_len):
            
            permutation = string[i:] + string[:i]
            BWT_perm.append(permutation)

        BWT_perm.sort()
        BWT_perm = [perm[-1] for perm in BWT_perm]

        # replace runs with numbers
        compressed_BWT = ''
        prev_char = ''

        counter = 1

        for char in BWT_perm:

            if prev_char == '':
                compressed_BWT = char
                prev_char = char

            else:
                if char == prev_char:
                    counter += 1
                elif (char != prev_char) and (counter > 1):     # new char encountered after a previously detected run
                    compressed_BWT = compressed_BWT + str(counter) + char
                    prev_char = char
                    counter = 1                                 # reset counter to 1
                elif (char != prev_char) and (counter == 1):    # new char encountered with no run
                    compressed_BWT = compressed_BWT + char
                    prev_char = char
        
        if counter > 1: # check if the last character was a run
            compressed_BWT = compressed_BWT + str(counter)
        
        self.seq = compressed_BWT
    

    ### uncompress method using first-last property
    def uncompress(self):

        BWT_string = self.parse(self.seq)   # call in parse() method to unpack the numbers
        
        BWT_leftcol, BWT_rightcol = self.generate_BWT_cols(BWT_string)

        word = '$'
        word_len = len(BWT_string)
        curr_char = ''.join([char for char in BWT_leftcol if char[1] == '$'])

        for i in range(0,word_len-1):
            next_char_idx = BWT_rightcol.index(curr_char)
            curr_char = BWT_leftcol[next_char_idx]
            word = word + curr_char[-1]
        
        word = word.strip('$')
        
        self.seq = word


    ### Use BWT for pattern matching
    def find(self, query):

        # check if DNA object has been compressed
        compressed = False
        i = 0

        while (compressed == False) and (i < len(self.seq)):
            try:
                into_int = int(self.seq[i])
                compressed = True
            except ValueError:
                i += 1
                pass
        
        # compress via BWT if it is not compressed
        if compressed == False:
            self.compress() # apply compress() method to self
            BWT_comp = self.seq
        elif compressed == True:
            BWT_comp = self.seq

        BWT_string = self.parse(BWT_comp)
        
        # generate the left and right columns of the BWT matrix
        BWT_leftcol, BWT_rightcol = self.generate_BWT_cols(BWT_string)

        match_pos = []  # take note of the match positions

        # find matches using first-last property
        for char in query:

            new_match_pos = []
            
            # initialize
            if match_pos == []:

                for row in BWT_leftcol:
                    if char == row[-1]:
                        match_pos.append([row])
                    else:
                        pass
            
            elif match_pos != []:

                for match in match_pos:
                    leftcol_idx = BWT_rightcol.index(match[-1])
                    leftcol = BWT_leftcol[leftcol_idx]
                    if char == leftcol[-1]:
                        extended_match = list.copy(match)
                        extended_match.append(leftcol)
                        new_match_pos.append(extended_match)
                    else:
                        pass

                match_pos = new_match_pos # update with smaller list of matches

        # just keep start positions - !!! think of hashing this for performance
        match_pos = [match[0] for match in match_pos]
        start_indices = []
        
        # recover actual word but keep track of start positions
        word = '$'
        word_len = len(BWT_string)
        curr_char = ''.join([char for char in BWT_leftcol if char[1] == '$'])

        idx = 0

        for i in range(0,word_len-1):
            next_char_idx = BWT_rightcol.index(curr_char)
            curr_char = BWT_leftcol[next_char_idx]
            word = word + curr_char[-1]
            
            if curr_char in match_pos:
                start_indices.append(idx)
                idx += 1
            else:
                idx += 1
        
        word = word.strip('$')
        
        # print the alignments
        query_len = len(query)
        word_len = len(word)
        print(f'pattern alignment ({query}): ')
        print(word)
        for start in start_indices:
            print('-'*start + query + '-'*(word_len - query_len - start))



### TESTING SECTION ###

DNA_STRING = DNA('SHE SELLS SEASHELLS ON THE SEASHORE')
DNA_STRING.find('SE')


