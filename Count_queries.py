#%% In this file we use to count and find average query words.
def count_words_in_line(line):
    words = line.split()
    return len(words)

query_file_path = "queries.txt"


line_count = 0
total_words_count = 0


with open(query_file_path, "r", encoding="utf-8", errors="ignore") as query_file:
    for line in query_file:
        line = line.strip()  

       
        if line:
            line_count += 1
            total_words_count += count_words_in_line(line)


average_words_per_line = total_words_count / line_count if line_count > 0 else 0

print("Number of queries:", line_count)
print("Average words per query:", average_words_per_line)
