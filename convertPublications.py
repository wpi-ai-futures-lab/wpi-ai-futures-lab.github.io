import os
import bibtexparser
import frontmatter
import copy

for file in os.listdir("./bibs"):
    print(os.fsdecode(file))
    parsed = bibtexparser.parse_file("./bibs/" + file)
    print(parsed.entries[0]["title"])
    print([str.strip() for str in parsed.entries[0]["author"].split("and\n")])
    print(parsed.entries[0]["year"])
    post = frontmatter.loads("""
    ---
    ---
    """)
    post.content = ""
    post["year"] = parsed.entries[0]["year"]
    post["link"] = parsed.entries[0]["url"]
    post["members"] = [str.strip() for str in parsed.entries[0]["author"].split("and\n")]
    print(frontmatter.dumps(post))
    with open("./_publications/" + parsed.entries[0]["title"].replace(':', '') + ".md", "w") as f:
        f.write(frontmatter.dumps(post))
    # newParsed = copy.deepcopy(parsed)
    # newParsed.entries = parsed.entries[0]
    print(parsed.entries[0])
    # print(bibtexparser.write_string(newParsed))