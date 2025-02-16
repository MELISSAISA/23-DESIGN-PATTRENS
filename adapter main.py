from vehicles import Car, Motorcycle
import traceback

if __name__ == '__main__':
    car = Car()
    bike = Motorcycle()

    print("The Motorcycle\n")
    bike.assign_rider("hanane")
    bike.rev_throttle()
    bike.pull_brake_lever()
    print("\n")

    print("The Car\n")
    car.assign_driver("romaissa")
    car.accelerate()
    car.apply_brakes()
    print("\n")

    print("Attempting to call car methods on a motorcycle object\n")

    try:
        bike.assign_driver("Robert")  # Wrong method for a motorcycle
        bike.accelerate()  # Motorcycles don't have `accelerate()`
        bike.apply_brakes()  # Motorcycles don't have `apply_brakes()`
    except AttributeError:
        print("Oops! The bike object cannot access car methods.")
        traceback.print_exc()
