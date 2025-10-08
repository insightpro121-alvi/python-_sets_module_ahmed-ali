friuts={"apple",'bannana',"mango","gava"}

try:
    friuts.remove("grapes")
except KeyError as e:
    print("remove()rasied KeyError:",e)

friuts.discard("grapes")
print("discard ()did not raise an error")

