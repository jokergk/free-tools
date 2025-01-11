
import random
import csv

def generate_phone_numbers(total_length, country_code, local_code, limit):
    phone_numbers = []
    # Calculate the remaining length for the number after country and local codes
    remaining_length = total_length - len(country_code) - len(local_code)
    if remaining_length <= 0:
        raise ValueError("Total length is too short for the specified country and local codes.")
    
    for _ in range(limit):
        number = "".join([str(random.randint(0, 9)) for _ in range(remaining_length)])
        phone_numbers.append(f"{country_code}{local_code}{number}")
    return phone_numbers

def save_to_csv(phone_numbers, filename="phone_numbers.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Phone Number"])
        for number in phone_numbers:
            writer.writerow([number])

def main():
    print("Phone Number Generator")
    try:
        total_length = int(input("Enter the total length of the phone number us(1216213xxxx) (including country and local codes) without +: "))
        country_code = input("Enter the country code (e.g., +1, +91, +44): ")
        local_code = input("Enter the local code (e.g., 415, 011, 020): ")
        limit = int(input("Enter the number of phone numbers to generate: "))
        filename = input("Enter the output CSV file name (default: phone_numbers.csv): ").strip() or "phone_numbers.csv"
        
        phone_numbers = generate_phone_numbers(total_length, country_code, local_code, limit)
        save_to_csv(phone_numbers, filename)
        
        print(f"Successfully generated {limit} phone numbers of length {total_length} and saved to {filename}.")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
