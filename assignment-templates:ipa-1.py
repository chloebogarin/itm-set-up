def savings(gross_pay, tax_rate, expenses):
    final_pay=int(gross_pay-(tax_rate*gross_pay)-expenses)
    return final_pay
def material_waste(total_material, material_units, num_jobs, job_consumption):
    return str(total_material-(num_jobs*job_consumption))+str(material_units)
def interest(principal, rate, periods):
    return int(principal+(principal*rate*periods))
def body_mass_index(weight, height):
    weight_kg=weight*0.453592
    height_in=(height[0]*12)+height[1]
    height_meters=0.0254*height_in
    return weight_kg/(height_meters**2)



