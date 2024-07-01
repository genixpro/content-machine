import csv
import openai
import base64
import re
from google.cloud import storage
#
# storage_client = storage.Client()
# quickTakeImageBucket = storage_client.get_bucket("quick-take-images")

# client = openai.OpenAI(
#     api_key="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"
# )


def load_csv():
    items = []
    with open("client_education_shorts.csv", "r") as file:
        # Open with the DictReader
        reader = csv.DictReader(file)
        # Iterate over the rows
        for row in reader:
            items.append(row)

    return items


def save_csv(items):
    with open("client_education_shorts_processed.csv", "w") as file:
        # Open with the DictReader
        writer = csv.DictWriter(file, fieldnames=[
            "Number",
            "Title",
            "Question",
            "Answer",
        ])
        writer.writeheader()
        # Iterate over the rows
        for item in items:
            writer.writerow(item)


def output_teleprompter_text():
    items = load_csv()

    for item in items:
        print(f"Title: {item['Title']}")
        print(f"Question: {item['Question']}")
        print(f"Answer: {item['Answer']}")
        print("\n\n")


output_teleprompter_text()

#
# def generate_image(prompt):
#     """Generates an image using DALL-E."""
#     # Make the request up to OpenAI
#     response = client.images.generate(
#         model="dall-e-3",
#         prompt=prompt,
#         size="1792x1024",
#         quality="standard",
#         style="vivid",
#         response_format="b64_json",
#         n=1,
#     )
#
#     # Convert the response data into a bytes object
#     image_data_b64 = response.data[0].b64_json
#     image_data_bytes = base64.b64decode(image_data_b64)
#
#     # Return the bytes result
#     return image_data_bytes
#
#
# def generate_all_images():
#     items = load_csv()
#
#     # Only use the first three items for now
#     # items = items[:3]
#
#     # Now we can use the items list to generate the images
#     for item_index, item in enumerate(items):
#         # Format the item index as a three digit number
#         item_index_str = f"{item_index + 1:03d}"
#
#         item['Item Number'] = item_index_str
#
#         title = item["Title"]
#         broadTopic = item["Broad Topic"]
#         narrowTopic = item["Narrow Topic"]
#         question = item['Question']
#
#         # Now select a filename. Remove all symbols from the title using a regular expression
#         image_filename = item_index_str + " - " + re.sub(r"[^a-zA-Z0-9\s,]", "", title) + ".png"
#
#         # Check if the blob already exists
#         try:
#             image_data = quickTakeImageBucket.blob(image_filename).download_as_bytes()
#             print("Image already exists, moving on")
#
#             # Save the image locally
#             with open(image_filename, "wb") as file:
#                 file.write(image_data)
#             continue
#         except Exception as e:
#             pass
#
#         # Ok doesn't existing, lets generate and store it
#         prompt = f"""Please generate a cool, sci-fi image that represents the fear captured by the following question:
# Broad Topic: {broadTopic}
# Narrow Topic: {narrowTopic}
# Question: {question}
# """
#
#         print(f"Generated image with prompt {prompt}")
#
#         image_data = generate_image(prompt)
#         quickTakeImageBucket.blob(image_filename).upload_from_string(image_data)
#
#         print(f"Generated image for {title}")
#
#         # Save the image locally
#         with open(image_filename, "wb") as file:
#             file.write(image_data)
#
#         # Add in the URL to the data
#         item['image_url'] = f"https://storage.googleapis.com/quick-take-images/{image_filename}"
#
#         save_csv(items)
#
#
# generate_all_images()
