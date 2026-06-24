def give_tips(risk):
    print("\n----- PREVENTION TIPS -----")

    if risk == "HIGH":
        print("• Immediate lockdown")
        print("• Mask mandate")
        print("• Vaccination drive")
        print("• Travel restrictions")
        print("• Schools closed")

    elif risk == "MEDIUM":
        print("• Masks in crowded places")
        print("• Social distancing")
        print("• Work from home")

    else:
        print("• Maintain hygiene")
        print("• Awareness campaigns")
        print("• Monitor symptoms")