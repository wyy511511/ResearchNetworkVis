import bibtexparser
from collections import Counter

# 读取 BibTeX 文件
with open('zotero.bib', encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# 提取所有作者
all_authors = []
for entry in bib_database.entries:
    if 'author' in entry:
        authors = entry['author'].split(' and ')
        all_authors.extend(authors)

# 去重并统计
author_counter = Counter(all_authors)
sorted_authors = author_counter.most_common()

# 输出统计结果
print(f"Total unique authors: {len(sorted_authors)}")
for author, count in sorted_authors:
    print(f"{author}: {count}")

# 如果你需要将结果保存到文件中
with open('author_statistics.txt', 'w', encoding='utf-8') as f:
    f.write(f"Total unique authors: {len(sorted_authors)}\n")
    for author, count in sorted_authors:
        f.write(f"{author}: {count}\n")