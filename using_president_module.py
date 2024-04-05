from president import President

p = President(26)
print(f"{p = }\n")
print(f"{p.first_name = }")
print(f"{p.last_name = }")
print(f"{dir(p) = }")

#  obj.attr_name  

print(f"{getattr(p, 'party') = }")
print(f"{hasattr(p, 'first_name') = }")
print(f"{hasattr(p, 'favorite_color') = }")

def get_full_name(self):
    return f"{self.first_name} {self.last_name}"

setattr(President, "full_name", property(get_full_name))

print(f"{p.full_name = }")


