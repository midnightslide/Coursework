about_me = {"name": "Greg",
            "age": "34",
            "hobbies": ["Programming", "cars", "etc"],
            "wake": {"monday":  "6am",
                     "tuesday":  "6am"
                    }
            }
print(f'{about_me["name"]} is {about_me["age"]} years old. He enjoys {about_me[hobbies]} and wakes up at {about_me[wake][2]}')
