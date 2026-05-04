from PIL import Image,ImageFilter
from io import BytesIO
import requests
from concurrent.futures import ProcessPoolExecutor

def download_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

def apply_effect(image):
    # Simulate a CPU-intensive task by applying a Gaussian blur effect
    return image.filter(ImageFilter.GaussianBlur(radius=2))

def process_image(image_url):
    image = download_image(image_url)
    image2 = apply_effect(image)
    print(f"Processed image with size {image2.size}")
    image.save(f"processed_{image_url.split('/')[-1]}.png")
    return image2
if __name__ == "__main__":
    image_urls = [
    "https://www.val-gardena.com/fileadmin/_processed_/8/5/csm_2020-09-09-jb-pic_c31fd6a4c2.jpg",
    "https://static.vecteezy.com/system/resources/thumbnails/036/333/113/small_2x/monarch-beautiful-butterflygraphy-beautiful-butterfly-on-flower-macrography-beautyful-nature-photo.jpg",
    "https://static.vecteezy.com/system/resources/thumbnails/071/827/814/small_2x/toyota-4runner-exploring-the-amazon-rainforests-lush-trails-free-photo.jpg",
    # Add more URLs as needed
    ]

    with ProcessPoolExecutor() as executor:
        processed_images = list(executor.map(process_image, image_urls))
    print("Image processing completed.")