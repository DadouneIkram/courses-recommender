def apriori_recommend(rules, input_courses):
    input_courses_set = set(input_courses)
    
    rules['antecedents'] = rules['antecedents'].apply(eval)
    rules['consequents'] = rules['consequents'].apply(eval)
    
    matching_rules = rules[rules['antecedents'].apply(lambda x: input_courses_set.issubset(x))]
    
    if matching_rules.empty:
        return None
    
    matching_rules = matching_rules.sort_values(['confidence', 'lift'], ascending=[False, False])
    
    recommendations = set()
    for consequent in matching_rules['consequents']:
        recommendations.update(consequent)
    
    recommendations.difference_update(input_courses_set)
    
    return recommendations
