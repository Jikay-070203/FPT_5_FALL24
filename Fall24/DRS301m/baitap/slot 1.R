#tạo một vector chứa các số nguyên từ 1 đến 5 
my_vector <-c(1,2,3,4,5)
print(my_vector)

#tạo một vector chứa các chuỗi ký tự 
my_string_vector <- c("apple","banana","orange")
print(my_string_vector)

#tạo một vector chứa các số thực 
my_numric_vector <-c(3.14,2.718,1.618)
print(my_numric_vector)

#kết hợp các loại dữ liệu khác nhau vào một vector
mixed_vector <-seq(from = 1,to = 9 ,by =2)
print(mixed_vector)


# Tạo một vector chứa các số nguyên từ 1 đến 10
my_vector <- 1:10
print(my_vector)

# Tạo một vector chứa các số chẵn từ 2 đến 10
even_vector <- seq(from = 2, to = 10, by = 2)
print(even_vector)

# Tạo một vector chứa các số lẻ từ 1 đến 9
odd_vector <- seq(from = 1, to = 9, by = 2)
print(odd_vector)



# ví dụ về cách sử dụng hàm seq() trong R để tạo các vector:

# Tạo một vector chứa các số từ 1 đến 10:
my_vector <- seq(1, 10)
print(my_vector)

# Tạo một vector chứa các số từ 0 đến 1 với bước nhảy là 0.1:
my_vector <- seq(0, 1, by = 0.1)
print(my_vector)

# Tạo một vector chứa 5 phần tử cách đều nhau trong khoảng từ 1 đến 10:
my_vector <- seq(1, 10, length.out = 5)
print(my_vector)

# Tạo một vector chứa các số từ 10 đến 1:
my_vector <- seq(10, 1)
print(my_vector)

------------
#Tao du lieu mau
names <- c("Nhường","Huy","Lâm","Bôn","Toàn")
genders <- c("female","male","male","male","female")
ages <- c(25,30,35,40,45)

#Tao mang tu mot vector
people_vector <- c(names,genders,ages)
#Tao mang tu vector voi kich thuoc va chieu co the thay doi
people_array <- array(data = people_vector, dim = c(3,5))

#Dat ten cho cac hang va cot cua mang
dimnames(people_array)<-list(c("Name","Gender","Age"),c("1","2","3","4","5"))

#In mang
print("Mang thong tin ve nhom nguoi:")
print(people_array)



-------------------------
#hàm readline()  được sử dụng để nhập dữ liệu từ bàn phím 

#nhập chuỗi từ bản phím 
input <- readline(prompt = "Nhập tên của bạn: ")
print(paste("Tên của bạn là", input))


#nhập nhiều giá trị từ bàn phím 
numbers <- scan()
print(numbers)

```{r}
# Nhập nhiều giá trị từ bàn phím
numbers <- scan()
print(numbers)
```

a.read.table()
```{r}
#đọc dữ liệu từ 1 tệp
data <- read.table("D:/FPT_ok/Kì học/fall2024/DRS301m/data1/vi du text file.txt",header = TRUE)
print(data)
```
b.read.csv()
đọc dữ lieu từ csv thường dùng dấu phẩy để phân tách các cột 
#{r}
#đọc dữ liệu từ tệp Csv
data <- read.csv("D:/FPT_ok/Kì học/fall2024/DRS301m/data1/raw_seoul_bike_sharing.csv",header = TRUE)
print(data)

------
  #đọc dữ liệu từ tệp được phân tách bởi tab
data <- read.delim("D:/FPT_ok/Kì học/fall2024/DRS301m/data1/vi du file dang tab.tsv",header = TRUE)
print(data)

-----
3.read.xlsx() trong thư viện openxlsx để nhập dữ liệu từ excel mà kg cần cài java

#cài thư viện openxlsx
install.packages("openxlsx")
library(openxlsx)
update.packages()

#đọc dữ liệu từ excel
data <- read.xlsx("D:/FPT_ok/Kì học/fall2024/DRS301m/data1/Telco_customer_churn.xlsx")
print(data)