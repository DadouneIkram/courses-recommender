def fp_growth_recommend(rules, input_courses):
    input_courses_set = set(input_courses)
    recommendations = set()

    for _, rule in rules.iterrows():
        antecedents = eval(rule['antecedents'])
        consequents = eval(rule['consequents'])
        
        if input_courses_set.issubset(antecedents):
            recommendations.update(consequents)

    return recommendations - input_courses_set