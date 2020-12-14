from mrjob.job import MRJob

class text_count(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == "python":
                yield "python", 1

    def reducer(self, key, values):
        yield key, sum(values)            

if __name__ == "__main__":
   text_count.run()