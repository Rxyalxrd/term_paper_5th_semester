#include <iostream>
extern "C" bool convert(int num, int radix, char *buf);
using namespace std;
int main()
{
	setlocale(LC_ALL, "Russian");//������� ������
	int a, rdx;
	char buf[64];
	//���� �������� ������
	cout << "������� �����: ";
	cin >> a;
	cout << "� ����� ������� ��������� ��������� (2-36): ";
	cin >> rdx;
	//��������������
	bool r = convert(a, rdx, buf);
	//����� ����������
	if (r)
	{
		cout << a << " � ������� ��������� � ���������� " << rdx << " ����� " << buf << endl;
	}
	else
	{
		cout << "������ ��������������" << endl;
	}
	system("pause");
	return 0;
}