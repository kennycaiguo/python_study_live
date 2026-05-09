import base64

def image_to_base64(image_path):
    """将图片文件转换为 Base64 编码的字符串"""
    try:
        with open(image_path, "rb") as image_file:
            # 读取图片的二进制数据
            binary_data = image_file.read()
            # 编码为 Base64 字节串，再转为字符串
            base64_encoded = base64.b64encode(binary_data).decode('ascii')
            return base64_encoded
    except FileNotFoundError:
        print(f"错误：找不到文件 {image_path}")
        return None
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return None
    

def base64_to_image(base64_string, output_path):
    """将 Base64 字符串解码并保存为图片文件"""
    try:
        # 将 Base64 字符串解码为字节串
        binary_data = base64.b64decode(base64_string)
        # 将字节串写入文件
        with open(output_path, "wb") as output_file:
            output_file.write(binary_data)
        print(f"图片已成功保存为 {output_path}")
    except Exception as e:
        print(f"保存文件时发生错误: {e}")    

if __name__ == '__main__':
    img_path = "./1.jpg"
    img_str = image_to_base64(img_path)
    # print(img_str)
    img = base64_to_image(img_str,"2.jpg")