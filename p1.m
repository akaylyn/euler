
i = 0
sum = 0

while i < 1000,
	flag = false;
	if mod(i, 3)==0,
		flag = true;
	end;
	if mod(i, 5)==0,
		flag = true;
	end;
	if flag == true,
		sum += i;
	end;
	i++;
end;

sum = sum