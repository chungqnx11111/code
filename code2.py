import pandas as pd

# (2d) Tạo DataFrame chứa thông tin ban đầu
data = {
    "TÊN": ["Python", "Java", "C++", "Ruby", "JavaScript"],
    "NĂM": [1991, 1995, 1985, 1995, 1995],
    "NGƯỜI SÁNG TẠO": [
        "Guido van Rossum",
        "James Gosling",
        "Bjarne Stroustrup",
        "Yukihiro Matsumoto",
        "Brendan Eich"
    ],
    "KIỂU LẬP TRÌNH": [
        "Hướng đối tượng",
        "Hướng đối tượng",
        "Thủ tục",
        "Hướng đối tượng",
        "Hướng sự kiện"
    ]
}

df = pd.DataFrame(data)

# (2d) Thêm ngôn ngữ mới: Go
df = pd.concat([df, pd.DataFrame({
    "TÊN": ["Go"],
    "NĂM": [2009],
    "NGƯỜI SÁNG TẠO": ["Robert Griesemer"],
    "KIỂU LẬP TRÌNH": ["Thủ tục"]
})], ignore_index=True)

print("DataFrame sau khi thêm ngôn ngữ Go:")
print(df)

# (1d) Sửa kiểu lập trình của JavaScript
df.loc[df["TÊN"] == "JavaScript", "KIỂU LẬP TRÌNH"] = "Chức năng, Hướng sự kiện"

# (1d) Xóa Ruby
df = df[df["TÊN"] != "Ruby"]

# (1d) Lọc các ngôn ngữ ra đời sau 1990
print("\nNgôn ngữ lập trình ra đời sau năm 1990:")
print(df[df["NĂM"] > 1990])

# (1d) Đếm số ngôn ngữ ra đời năm 1995 và kiểu lập trình là 'Hướng đối tượng'
count = df[(df["NĂM"] == 1995) & (df["KIỂU LẬP TRÌNH"] == "Hướng đối tượng")].shape[0]
print(f"\nSố ngôn ngữ ra đời năm 1995 và thuộc kiểu 'Hướng đối tượng': {count}")

# (1d) Sắp xếp theo thứ tự tăng dần của NĂM
df_sorted = df.sort_values(by="NĂM", ascending=True)
print("\nDataFrame sau khi sắp xếp theo năm tăng dần:")
print(df_sorted)

# (1d) Ghi dữ liệu ra file NNLT.csv
df_sorted.to_csv("NNLT.csv", index=False, encoding="utf-8-sig")

