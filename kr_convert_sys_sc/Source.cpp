#include <iostream>
extern "C" bool convert(int num, int radix, char *buf);
using namespace std;
int main()
{
	setlocale(LC_ALL, "Russian");//русская локаль
	int a, rdx;
	char buf[64];
	//ввод исходных данных
	cout << "Введите число: ";
	cin >> a;
	cout << "В какую систему счисления перевести (2-36): ";
	cin >> rdx;
	//преобразование
	bool r = convert(a, rdx, buf);
	//вывод результата
	if (r)
	{
		cout << a << " в системе счисления с основанием " << rdx << " равно " << buf << endl;
	}
	else
	{
		cout << "Ошибка преобразования" << endl;
	}
	system("pause");
	return 0;
}