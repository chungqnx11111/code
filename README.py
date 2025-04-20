# Hàm tính điểm cuối
def calculate_final_grade(midterm, final_exam):
    return midterm * 0.4 + final_exam * 0.6

# Chương trình chính
def main():
    students = []
    
    while True:
        # Nhập thông tin sinh viên
        student_id = input("Nhập mã sinh viên (hoặc gõ 'exit' để kết thúc): ")
        if student_id.lower() == 'exit':
            break
        
        name = input("Nhập tên sinh viên: ")
        midterm_score = float(input("Nhập điểm thi giữa kỳ: "))
        final_exam_score = float(input("Nhập điểm thi cuối kỳ: "))
        
        # Tính điểm cuối
        final_grade = calculate_final_grade(midterm_score, final_exam_score)
        
        # Lưu thông tin sinh viên
        students.append({
            "ID": student_id,
            "Name": name,
    
    
            "Midterm": midterm_score,
            "Final Exam": final_exam_score,
            "Final Grade": final_grade
        })
    
    # Xuất danh sách sinh viên và điểm cuối
    print("\nDanh sách sinh viên và điểm cuối:")
    for student in students:
        print(f"Mã: {student['ID']}, Tên: {student['Name']}, Điểm cuối: {student['Final Grade']:.2f}")

    # Tìm sinh viên có điểm cuối >= 8.0 và điểm giữa kỳ < 5
    print("\nDanh sách sinh viên có điểm cuối >= 8.0 và điểm giữa kỳ < 5:")
    for student in students:
        if student["Final Grade"] >= 8.0 and student["Midterm"] < 5:
            print(f"Mã: {student['ID']}, Tên: {student['Name']}")

if __name__ == "__main__":
    main()
