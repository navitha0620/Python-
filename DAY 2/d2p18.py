#DICTIONARY
#IN A DICTIONARY WE CAN STORE "key: value" PAIRS AS AN ELEMENTS
#WE CAN CREATE DICTIONARY EITHER BY USING CURLY BRACES{} or "dict class"
#MUTABLE OBJECTS
#Keys must be unique
#WE HAVE TO USE IMMUTABLE OBJECTS AS A KEY

d1={1:"Navitha",
    1:"Navi",
    1:"vitha",
    1:"vitha Navi",
    1:"Navi Vitha",
    1:"Na Vitha"
}
print(d1)
#KEY should be unique otherwise , it will print last element


d2={1:"Navitha",
    2:"Navi",
    3:"vitha",
    4:"vitha Navi",
    5:"Navi Vitha",
    6:"Na Vitha",
    #[10,20]:"Heeeeee"---->TypeError : unhashable type :"list"
    (10,20):"Heeeee"#AS a "key"  "IMMUTABLE" objects can be used like "tuple"
}
print(d2)
