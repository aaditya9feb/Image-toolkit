from PIL import Image, ImageOps

def load_image(path):
    return Image.open(path)

def show_image(img):
    img.show()

def rotate_image(img, angle):
    return img.rotate(angle)

def grayscale_image(img):
    return ImageOps.grayscale(img)

def resize_image(img, width, height):
    return img.resize((width, height))

def save_image(img, path):
    img.save(path)

def main():
    img = None

    while True:
        print("\nChoose an operation:")
        print("1. Load image")
        print("2. Show image")
        print("3. Rotate image")
        print("4. Convert to grayscale")
        print("5. Resize image")
        print("6. Save image")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "1":
            path = input("Enter image path: ")
            try:
                img = load_image(path)
                print("Image loaded.")
            except:
                print("Failed to load image.")
        elif choice == "2":
            if img:
                show_image(img)
            else:
                print("No image loaded.")
        elif choice == "3":
            if img:
                angle = float(input("Enter angle to rotate: "))
                img = rotate_image(img, angle)
                print("Image rotated.")
            else:
                print("No image loaded.")
        elif choice == "4":
            if img:
                img = grayscale_image(img)
                print("Image converted to grayscale.")
            else:
                print("No image loaded.")
        elif choice == "5":
            if img:
                width = int(input("Enter new width: "))
                height = int(input("Enter new height: "))
                img = resize_image(img, width, height)
                print("Image resized.")
            else:
                print("No image loaded.")
        elif choice == "6":
            if img:
                save_path = input("Enter filename to save as: ")
                try:
                    save_image(img, save_path)
                    print("Image saved.")
                except:
                    print("Failed to save image.")
            else:
                print("No image loaded.")
        elif choice == "7":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
