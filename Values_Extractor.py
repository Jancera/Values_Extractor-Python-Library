class Values_Extractor:
    """

    The code will return the values with the measurements units converted according to the S.I


    text_to_extract is the text that you want to extract the values.



    classification_type can be 'time', 'distance', 'speed' and it defines what type of results you want.



    all_printed=True is to print all results that the algorithm found.

    Examples
    --------
    Input:


    text = I have only 1 minute

    a = Values_Extractor(text, classification_time='time', all_printed=True)

    x = extractor()


    Output:

    x will be equal one list with the values [60 sec]

    In your terminal will be printed 60 sec too

    See also
    --------
    My youtube channel with a video explaining :
    My github repository if you want to help me making some pull requests :
    """

    def __init__(
            self,
            text_to_extract=None,
            classification_type=None,
            all_printed=None,
    ):

        self.text = text_to_extract
        self.type = classification_type
        self.print_ = all_printed

    def extractor(self):
        self.text = self.text + '           '
        numbers_index = []
        numbers = '1 2 3 4 5 6 7 8 9 0 .'.split()
        time_pattern = ['hours ', 'hour ', ' hours ', ' hour ', ' h ', 'h ', ' minute', 'minute',
                        ' min ', 'min ', ' second', 'second', ' s ', 's ']

        distance_pattern = [' kilometer', 'kilometer', ' km ', 'km ', ' meter', 'meter', 'm ', ' m ', ' centim',
                            'centim', ' cm ', 'cm ', ' milim', 'milim', ' mm', 'mm']

        velocity_pattern = [' km/h', 'km/h', ' m/s', 'm/s']

        text_ = self.text.lower()
        count = 0
        text = [char for char in text_]
        if count == 0:
            copy_text = text
        for number in text:
            if number in numbers:
                num1 = text.index(number)
                text = text[(num1 + 1):]
                numbers_index.append(num1)
                continue
            count = count + 1
        for predecessor_num in numbers_index[1:]:
            ind = (numbers_index.index(predecessor_num) - 1)
            if predecessor_num < numbers_index[ind] or predecessor_num > numbers_index[ind] and predecessor_num != 0:
                a_ = predecessor_num + numbers_index[ind]
                numbers_index[numbers_index.index(predecessor_num)] = a_ + 1
            else:  # a_ == 0:
                numbers_index[numbers_index.index(predecessor_num)] = numbers_index[ind] + 1

            # It is to let the indexes equals, because of the logic used above was to cut my main list every time the
            # code found one number, so here I am leaving all indexes equivalent to the main list

        # Until here is to get the indexes of the numbers

        numbers_index.append(-1)
        classifiers = []
        consecutive_numbers = []
        for element in numbers_index:
            if element != -1:
                if numbers_index[numbers_index.index(element) + 1] == element + 1:
                    consecutive_numbers.append(element)
                    consecutive_numbers.append(element + 1)

            text_after = []
            for letter in range(element + 1, element + 11):
                text_after.append(copy_text[letter])
            text_after = ''.join(text_after)
            classifiers.append(text_after)

            # Getting the classifiers, the measurement units

        consecutive_numbers = list(dict.fromkeys(consecutive_numbers))  # Because of I added to my consecutive_numbers
        # list (line 58-59) the consecutive numbers 2 times now I need to delete repeated numbers.
        consecutive_numbers.append(-1)  # Avoiding errors

        for index in consecutive_numbers:

            if index != -1:

                if index + 1 == consecutive_numbers[consecutive_numbers.index(index) + 1]:
                    continue
                else:
                    some = consecutive_numbers[:consecutive_numbers.index(index) + 1]
                    consecutive_numbers = consecutive_numbers[consecutive_numbers.index(index) + 1:]
                    for i in range(len(some) - 1):
                        numbers_index.remove(numbers_index[numbers_index.index(some[i])])
                    numbers_index[numbers_index.index(int(some[-1]))] = -2
                    for i in some:
                        some[some.index(i)] = copy_text[i]
                    y = ''.join(some)
                    numbers_index[numbers_index.index(-2)] = float(y) * -1

                    # Slicing the list of consecutive numbers, getting one consecutive number per time
                    # Transforming the indexes into the real number and multiplying by -1

        final_values = []
        count = 0

        for word in classifiers:

            if word[:8] in time_pattern or word[:7] in time_pattern or word[:6] in time_pattern or \
                    word[:5] in time_pattern or word[:4] in time_pattern or word[:3] in time_pattern \
                    or word[:2] in time_pattern:

                if numbers_index[count] < 0 and numbers_index[count] != -1:
                    if word[:6] == 'hours ' or word[:5] == 'hour ' or word[:7] == ' hours ' or word[:6] == ' hour ' or \
                            word[:3] == ' h ' or word[:2] == 'h ':
                        final_values.append([float(numbers_index[count]) * -3600, ' sec'])
                        count = count + 1

                    elif word[:7] == ' minute' or word[:6] == 'minute' or word[:5] == ' min ' or word[:4] == 'min ':
                        final_values.append([float(numbers_index[count]) * -60, ' sec'])
                        count = count + 1

                    elif word[:8] == ' second' or word[:7] == 'second' or word[:3] == ' s ' or word[:2] == 's ':
                        final_values.append([float(numbers_index[count]) * -1, ' sec'])
                        count = count + 1
                else:

                    if word[:6] == 'hours ' or word[:5] == 'hour ' or word[:7] == ' hours ' or word[:6] == ' hour ' or \
                            word[:3] == ' h ' or word[:2] == 'h ':
                        final_values.append([float(copy_text[numbers_index[count]]) * 3600, ' sec'])
                        count = count + 1

                    elif word[:7] == ' minute' or word[:6] == 'minute' or word[:5] == ' min ' or word[:4] == 'min ':
                        final_values.append([float(copy_text[numbers_index[count]]) * 60, ' sec'])
                        count = count + 1

                    elif word[:8] == ' second' or word[:7] == 'second' or word[:3] == ' s ' or word[:2] == 's ':

                        final_values.append([float(copy_text[numbers_index[count]]), ' sec'])
                        count = count + 1

            if word[:10] in distance_pattern or word[:9] in distance_pattern or word[:7] in distance_pattern or \
                    word[:6] in distance_pattern or word[:5] in distance_pattern or word[:4] in distance_pattern or \
                    word[:3] in distance_pattern or word[:2]:
                if numbers_index[count] < 0 and numbers_index[count] != -1:

                    if word[:10] == ' kilometer' or word[:9] == 'kilometer' or word[:4] == ' km ' or word[:3] == 'km ':
                        final_values.append([(float(numbers_index[count]) * -1000), ' m'])
                        count = count + 1

                    elif word[:6] == ' meter' or word[:5] == 'meter' or word[:2] == 'm ' or word[:3] == ' m ':
                        final_values.append([(float(numbers_index[count]) * -1), ' m'])
                        count = count + 1

                    elif word[:7] == ' centim' or word[:6] == 'centim' or word[:4] == ' cm ' or word[:3] == 'cm ':
                        final_values.append([(float(numbers_index[count]) / -100), ' m'])
                        count = count + 1

                    elif word[:6] == ' milim' or word[:5] == 'milim' or word[:3] == ' mm' or word[:2] == 'mm':
                        final_values.append([(float(numbers_index[count]) / -1000), ' m'])
                        count = count + 1
                else:

                    if word[:10] == ' kilometer' or word[:9] == 'kilometer' or word[:4] == ' km ' or word[:3] == 'km ':
                        final_values.append([(float(copy_text[numbers_index[count]]) * 1000), ' m'])
                        count = count + 1

                    elif word[:6] == ' meter' or word[:5] == 'meter' or word[:2] == 'm ' or word[:3] == ' m ':
                        final_values.append([float(copy_text[numbers_index[count]]), ' m'])
                        count = count + 1


                    elif word[:7] == ' centim' or word[:6] == 'centim' or word[:4] == ' cm ' or word[:3] == 'cm ':

                        final_values.append([(float(copy_text[numbers_index[count]]) / 100), ' m'])
                        count = count + 1

                    elif word[:6] == ' milim' or word[:5] == 'milim' or word[:3] == ' mm' or word[:2] == 'mm':
                        final_values.append([(float(copy_text[numbers_index[count]]) / 1000), ' m'])
                        count = count + 1

            if word[:5] in velocity_pattern or word[:4] in velocity_pattern or word[:3] in velocity_pattern:
                if numbers_index[count] < 0 and numbers_index[count] != -1:

                    if word[:5] == ' km/h' or word[:4] == 'km/h':
                        final_values.append([float(numbers_index[count]) / -3.6, ' m/s'])
                        count = count + 1

                    elif word[:4] == ' m/s' or word[:3] == 'm/s':
                        final_values.append([float(numbers_index[count]) * -1, ' m/s'])
                        count = count + 1
                else:

                    if word[:5] == ' km/h' or word[:4] == 'km/h':
                        final_values.append([float(copy_text[numbers_index[count]]) / 3.6, ' m/s'])
                        count = count + 1

                    elif word[:4] == ' m/s' or word[:3] == 'm/s':
                        final_values.append([float(copy_text[numbers_index[count]]), ' m/s'])
                        count = count + 1
                    # If the number is negative it means that is one consecutive number and I need to get it from
                    # numbers_index and not from my main text

        result = []
        temp = []

        if self.type == 'time':
            for i in final_values:
                if i[1] == ' sec':
                    temp.append(i)
            if self.print_:
                for i in temp:
                    print(str(i[0]) + i[1])
            return temp

        if self.type == 'distance':
            for i in final_values:
                if i[1] == ' m':
                    temp.append(i)
            if self.print_:
                for i in temp:
                    print(str(i[0]) + i[1])
            return temp

        if self.type == 'speed':
            for i in final_values:
                if i[1] == ' m/s':
                    temp.append(i)
            if self.print_:
                for i in temp:
                    print(str(i[0]) + i[1])
            return temp


        if self.type is None:
            for i in final_values:
                temp.append(i)
            if self.print_:
                for i in temp:
                    print(str(i[0]) + i[1])
            return final_values


