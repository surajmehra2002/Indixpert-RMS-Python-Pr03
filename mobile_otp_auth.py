import random
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

account_sid = 'AC204e5ad25ffe048e6ffcd02465ce13ac'
auth_token = '7d0b0874bac9e1c65290777fa06713d0'
twilio_phone_number = '+15595004669'

def generate_otp():
    return random.randint(100000, 999999)

def send_otp(mobile_number, otp):
    client = Client(account_sid, auth_token)
    
    try:
        message = client.messages.create(
            body=f"Your OTP is {otp}",
            from_=twilio_phone_number,
            to=mobile_number
        )
        print(f"OTP sent to {mobile_number}. Message SID: {message.sid}")
    except TwilioRestException as e:
        print(f"Failed to send OTP. Error: {e}")

def verify_otp(user_input_otp, actual_otp):
    return user_input_otp == actual_otp

if __name__ == "__main__":
    mobile_number = input("Enter your mobile number (with country code, e.g., +91...): ")
    otp = generate_otp()
    send_otp(mobile_number, otp)

    try:
        user_input_otp = int(input("Enter the OTP you received: "))
    except ValueError:
        print("Invalid input! Please enter a numeric OTP.")
        exit()

    if verify_otp(user_input_otp, otp):
        print("OTP verified successfully!")
    else:
        print("Invalid OTP. Please try again.")


# from twilio.rest import Client

# # Twilio credentials
# account_sid = 'AC204e5ad25ffe048e6ffcd02465ce13ac'
# auth_token = '7d0b0874bac9e1c65290777fa06713d0'
# client = Client(account_sid, auth_token)

# # Replace with your actual Message SID
# message_sid = 'SM00e0cebca3557240cb204235877d59a1'

# # Fetch the message
# message = client.messages(message_sid).fetch()

# # Print message details
# print(f"Message SID: {message.sid}")
# print(f"Body: {message.body}")
# print(f"From: {message.from_}")
# print(f"To: {message.to}")
# print(f"Status: {message.status}")
