def build_profile(first, last, **user_info):
    profile = {}
    profile['first-name'] = first
    profile['last-name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Kelcey', 'Lorenzo', initials='KLCL', role='technology-engineer', location='IRV', manager='MSM')
print(user_profile)