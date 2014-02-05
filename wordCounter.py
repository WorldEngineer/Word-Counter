'''The MIT License (MIT)

Copyright (c) 2014 Weston Hopkins

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.'''

#This function counts words and collects the lengths of those words along with
#the count in the dictionary "word_histogram". Punctuation appears as key "0".

def wordCounter(string):
        word_histogram = {}
        count = 0
        ignored_characters = [" ", "\'", "\"", "!", ",", ".", ":", ";", "?", "(", ")"]
	for x in string:
		if x not in ignored_characters:
                    count += 1
                elif count in word_histogram:
                    word_histogram[count] += 1
                    count = 0 
                else:
                    word_histogram[count] = 1
                    count = 0
        return word_histogram
