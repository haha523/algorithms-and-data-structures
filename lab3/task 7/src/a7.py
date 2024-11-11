def digital_sorting(n, m, k, data):
    # Chuyển đổi dữ liệu từ định dạng cột sang định dạng hàng
    strings = [''] * n
    for j in range(m):
        for i in range(n):
            strings[i] += data[j][i]

    # Tạo danh sách các chỉ số
    indices = list(range(1, n + 1))

    # Thực hiện k pha sắp xếp
    for phase in range(1, k + 1):
        # Sắp xếp theo ký tự ở vị trí m - phase
        indices.sort(key=lambda x: strings[x - 1][m - phase])

    return indices


# Đọc dữ liệu từ file input.txt
with open('input.txt', 'r') as f:
    n, m, k = map(int, f.readline().strip().split())
    data = [f.readline().strip() for _ in range(m)]

# Thực hiện sắp xếp
result = digital_sorting(n, m, k, data)

# Xuất kết quả ra file output.txt
with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, result)) + '\n')