import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-n","--name",required = True, help = "name of the user")

args = vars(ap.parse_args())
print(args)
print("Hi there {}, it's nice to meet you!".format(args["name"]))
