
import string

def count_words_in_file(file_path):
    word_count = {}
    
    # Mở file và đọc nội dung
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Chuyển tất cả thành chữ thường và loại bỏ dấu câu
            line = line.lower().translate(str.maketrans('', '', string.punctuation))
            
            # Tách dòng thành các từ
            words = line.split()
            
            # Đếm số lần xuất hiện của mỗi từ
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    
    return word_count
# gắn đường dẫn tới file .txt 
file_path = r'C:\Users\acer\OneDrive\Máy tính\Bt.CTDL.Giải Thuật\kt_18_2\P1_data.txt'
word_counts = count_words_in_file(file_path)
print(word_counts)
