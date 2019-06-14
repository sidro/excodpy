def compact(list_):
    return [comp for comp in list_ if comp]

print(compact([0,1,2,"",[], False, {}, None, "All done"]))
