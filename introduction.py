from datetime import datetime
Author = "DumpingTools"
Project = "Instagram security testing sandbox"
print("Project:\033[1;35;40m {}".format(Project))
print("\033[0;37;40m Author:\033[1;35;40m {}".format(Author))
d = datetime.date(datetime.now())
print("\033[0;37;40m Time:\033[1;31;40m {}".format(d))


