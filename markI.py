while(1):
	print "\n1.Length\n2.Area\n3.Volume\n4.Temperature\n5.Speed\n6.Time\n7.Mass\n"
	op=input("Select option number: ")
	while(op<1 or op>7):
		op=input("Enter a valid option (1 to 7): ")
#Length
	if(op==1):
		print "\n1.Kilometer(km)\n2.Meter(m)\n3.Centimeter(cm)\n4.Millimeter(mm)\n5.Micrometer\n6.Nanometer(nm)\n7.Picometer(pm)\n8.Mile(mi)\n9.Yard(yd)\n10.Foot(ft)\n11.Inch(in)\n12.Light Year(ly)"
		f=input("Select Unit to convert from: ")
		while(f<1 or f>12):
			f=input("Enter a valid option (1 to 12): ")
		x=input("Enter value to convert: ")
		print "\n1.Kilometer(km)\n2.Meter(m)\n3.Centimeter(cm)\n4.Millimeter(mm)\n5.Micrometer\n6.Nanometer(nm)\n7.Picometer(pm)\n8.Mile(mi)\n9.Yard(yd)\n10.Foot(ft)\n11.Inch(in)\n12.Light Year(ly)"
		t=input("Select Unit to convert to: ")
		while(t<1 or t>12):
			t=input("Enter a valid option (1 to 12): ")
	#km to
		if(f==1):
			if(t==1):
				y=x
				print x,"km = ",y,"km"
			elif(t==2):
				y=1000*x
				print x,"km = ",y,"m"
			elif(t==3):
				y=100000*x
				print x,"km = ",y,"cm"
			elif(t==4):
				y=1000000*x
				print x,"km = ",y,"mm"
			elif(t==5):
				y=100000000*x
				print x,"km = ",y,"micro m"
			elif(t==6):
				y=100000000000*x
				print x,"km = ",y,"nm"
			elif(t==7):
				y=100000000000000*x
				print x,"km = ",y,"pm"
			elif(t==8):
				y=0.621371192*x
				print x,"km = ",y,"mi"
			elif(t==9):
				y=1093.6133*x
				print x,"km = ",y,"yd"
			elif(t==10):
				y=3280.8399*x
				print x,"km = ",y,"ft"
			elif(t==11):
				y=39370.0787*x
				print x,"km = ",y,"in"
			else:
				y=1.057*(10**(-13))*x
				print x,"km = ",y,"ly"
	#m to
		elif(f==2):
			if(t==1):
				y=0.001*x
				print x,"m = ",y,"km"
			elif(t==2):
				y=x
				print x,"m = ",y,"m"
			elif(t==3):
				y=100*x
				print x,"m = ",y,"cm"
			elif(t==4):
				y=1000*x
				print x,"m = ",y,"mm"
			elif(t==5):
				y=1000000*x
				print x,"m = ",y,"micro m"
			elif(t==6):
				y=1000000000*x
				print x,"m = ",y,"nm"
			elif(t==7):
				y=1000000000000*x
				print x,"m = ",y,"pm"
			elif(t==8):
				y=0.000621371192*x
				print x,"m = ",y,"mi"
			elif(t==9):
				y=1.0936133*x
				print x,"m = ",y,"yd"
			elif(t==10):
				y=3.2808399*x
				print x,"m = ",y,"ft"
			elif(t==11):
				y=39.3700787*x
				print x,"m = ",y,"in"
			else:
				y=1.057*(10**(-16))*x
				print x,"m = ",y,"ly"
	#cm to
		elif(f==3):
			if(t==1):
				y=0.00001*x
				print x,"cm = ",y,"km"
			elif(t==2):
				y=0.01*x
				print x,"cm = ",y,"m"
			elif(t==3):
				y=x
				print x,"cm = ",y,"cm"
			elif(t==4):
				y=10*x
				print x,"cm = ",y,"mm"
			elif(t==5):
				y=10000*x
				print x,"cm = ",y,"micro m"
			elif(t==6):
				y=10000000*x
				print x,"cm = ",y,"nm"
			elif(t==7):
				y=10000000000*x
				print x,"cm = ",y,"pm"
			elif(t==8):
				y=0.00000621371192*x
				print x,"cm = ",y,"mi"
			elif(t==9):
				y=0.010936133*x
				print x,"cm = ",y,"yd"
			elif(t==10):
				y=0.032808399*x
				print x,"cm = ",y,"ft"
			elif(t==11):
				y=0.393700787*x
				print x,"cmm = ",y,"in"
			else:
				y=1.057*(10**(-18))*x
				print x,"cm = ",y,"ly"
	#mm to
		elif(f==4):
			if(t==1):
				y=0.000001*x
				print x,"mm = ",y,"km"
			elif(t==2):
				y=0.001*x
				print x,"mm = ",y,"m"
			elif(t==3):
				y=0.1*x
				print x,"mm = ",y,"cm"
			elif(t==4):
				y=x
				print x,"mm = ",y,"mm"
			elif(t==5):
				y=1000*x
				print x,"mm = ",y,"micro m"
			elif(t==6):
				y=1000000*x
				print x,"mm = ",y,"nm"
			elif(t==7):
				y=1000000000*x
				print x,"mm = ",y,"pm"
			elif(t==8):
				y=0.000000621371192*x
				print x,"mm = ",y,"mi"
			elif(t==9):
				y=0.0010936133*x
				print x,"mm = ",y,"yd"
			elif(t==10):
				y=0.0032808399*x
				print x,"mm = ",y,"ft"
			elif(t==11):
				y=0.0393700787*x
				print x,"mm = ",y,"in"
			else:
				y=1.057*(10**(-19))*x
				print x,"mm = ",y,"ly"
	#micro m to
		elif(f==5):
			if(t==1):
				y=0.000000001*x
				print x,"micro m = ",y,"km"
			elif(t==2):
				y=0.000001*x
				print x,"micro m = ",y,"m"
			elif(t==3):
				y=0.0001*x
				print x,"micro m = ",y,"cm"
			elif(t==4):
				y=0.001*x
				print x,"micro m = ",y,"mm"
			elif(t==5):
				y=x
				print x,"micro m = ",y,"micro m"
			elif(t==6):
				y=1000*x
				print x,"micro m = ",y,"nm"
			elif(t==7):
				y=1000000*x
				print x,"micro m = ",y,"pm"
			elif(t==8):
				y=0.000000000621371192*x
				print x,"micro m = ",y,"mi"
			elif(t==9):
				y=0.0000010936133*x
				print x,"micro m = ",y,"yd"
			elif(t==10):
				y=0.0000032808399*x
				print x,"micro m = ",y,"ft"
			elif(t==11):
				y=0.0000393700787*x
				print x,"micro m = ",y,"in"
			else:
				y=1.057*(10**(-22))*x
				print x,"micro m = ",y,"ly"
	#nm to
		elif(f==6):
			if(t==1):
				y=0.000000000001*x
				print x,"nm = ",y,"km"
			elif(t==2):
				y=0.000000001*x
				print x,"nm = ",y,"m"
			elif(t==3):
				y=0.0000001*x
				print x,"nm = ",y,"cm"
			elif(t==4):
				y=0.000001*x
				print x,"nm = ",y,"mm"
			elif(t==5):
				y=0.001*x
				print x,"nm = ",y,"micro m"
			elif(t==6):
				y=x
				print x,"nm = ",y,"nm"
			elif(t==7):
				y=1000*x
				print x,"nm = ",y,"pm"
			elif(t==8):
				y=0.000000000000621371192*x
				print x,"nm = ",y,"mi"
			elif(t==9):
				y=0.0000000010936133*x
				print x,"nm = ",y,"yd"
			elif(t==10):
				y=0.0000000032808399*x
				print x,"nm = ",y,"ft"
			elif(t==11):
				y=0.0000000393700787*x
				print x,"nm = ",y,"in"
			else:
				y=1.057*(10**(-25))*x
				print x,"nm = ",y,"ly"
	#pm to
		elif(f==7):
			if(t==1):
				y=0.000000000000001*x
				print x,"pm = ",y,"km"
			elif(t==2):
				y=0.000000000001*x
				print x,"pm = ",y,"m"
			elif(t==3):
				y=0.0000000001*x
				print x,"pm = ",y,"cm"
			elif(t==4):
				y=0.000000001*x
				print x,"pm = ",y,"mm"
			elif(t==5):
				y=0.000001*x
				print x,"pm = ",y,"micro m"
			elif(t==6):
				y=0.001*x
				print x,"pm = ",y,"nm"
			elif(t==7):
				y=x
				print x,"pm = ",y,"pm"
			elif(t==8):
				y=0.000000000000000621371192*x
				print x,"pm = ",y,"mi"
			elif(t==9):
				y=0.0000000000010936133*x
				print x,"pm = ",y,"yd"
			elif(t==10):
				y=0.0000000000032808399*x
				print x,"pm = ",y,"ft"
			elif(t==11):
				y=0.0000000000393700787*x
				print x,"pm = ",y,"in"
			else:
				y=1.057*(10**(-28))*x
				print x,"pm = ",y,"ly"
	#mi to
		elif(f==8):
			if(t==1):
				y=1.609344*x
				print x,"mi = ",y,"km"
			elif(t==2):
				y=1609.344*x
				print x,"mi = ",y,"m"
			elif(t==3):
				y=160934.4*x
				print x,"mi = ",y,"cm"
			elif(t==4):
				y=1609344*x
				print x,"mi = ",y,"mm"
			elif(t==5):
				y=1609344000*x
				print x,"mi = ",y,"micro m"
			elif(t==6):
				y=1609344000000*x
				print x,"mi = ",y,"nm"
			elif(t==7):
				y=1609344000000000*x
				print x,"mi = ",y,"pm"
			elif(t==8):
				y=x
				print x,"mi = ",y,"mi"
			elif(t==9):
				y=1760*x
				print x,"mi = ",y,"yd"
			elif(t==10):
				y=5280*x
				print x,"mi = ",y,"ft"
			elif(t==11):
				y=63360*x
				print x,"mi = ",y,"in"
			else:
				y=1.70107795*(10**(-13))*x
				print x,"mi = ",y,"ly"
	#yd to
		elif(f==9):
			if(t==1):
				y=0.0009144*x
				print x,"yd = ",y,"km"
			elif(t==2):
				y=0.9144*x
				print x,"yd = ",y,"m"
			elif(t==3):
				y=91.44*x
				print x,"yd = ",y,"cm"
			elif(t==4):
				y=914.4*x
				print x,"yd = ",y,"mm"
			elif(t==5):
				y=914400*x
				print x,"yd = ",y,"micro m"
			elif(t==6):
				y=914400000*x
				print x,"yd = ",y,"nm"
			elif(t==7):
				y=914400000000*x
				print x,"yd = ",y,"pm"
			elif(t==8):
				y=0.000568181818*x
				print x,"yd = ",y,"mi"
			elif(t==9):
				y=x
				print x,"yd = ",y,"yd"
			elif(t==10):
				y=3*x
				print x,"yd = ",y,"ft"
			elif(t==11):
				y=36*x
				print x,"yd = ",y,"in"
			else:
				y=9.66521563*(10**(-17))*x
				print x,"yd = ",y,"ly"
	#ft to
		elif(f==10):
			if(t==1):
				y=0.0003048*x
				print x,"ft = ",y,"km"
			elif(t==2):
				y=0.3048*x
				print x,"ft = ",y,"m"
			elif(t==3):
				y=30.48*x
				print x,"ft = ",y,"cm"
			elif(t==4):
				y=304.8*x
				print x,"ft = ",y,"mm"
			elif(t==5):
				y=304800*x
				print x,"ft = ",y,"micro m"
			elif(t==6):
				y=304800000*x
				print x,"ft = ",y,"nm"
			elif(t==7):
				y=(3.048*(10**11))*x
				print x,"ft = ",y,"pm"
			elif(t==8):
				y=0.000189393939*x
				print x,"ft = ",y,"mi"
			elif(t==9):
				y=0.33333333333333*x
				print x,"ft = ",y,"yd"
			elif(t==10):
				y=x
				print x,"ft = ",y,"ft"
			elif(t==11):
				y=12*x
				print x,"ft = ",y,"in"
			else:
				y=3.22173854*(10**(-17))*x
				print x,"ft = ",y,"ly"
	#in to
		elif(f==11):
			if(t==1):
				y=0.0000254*x
				print x,"in = ",y,"km"
			elif(t==2):
				y=0.0254*x
				print x,"in = ",y,"m"
			elif(t==3):
				y=2.54*x
				print x,"in = ",y,"cm"
			elif(t==4):
				y=25.4*x
				print x,"in = ",y,"mm"
			elif(t==5):
				y=25400*x
				print x,"in = ",y,"micro m"
			elif(t==6):
				y=25400000*x
				print x,"in = ",y,"nm"
			elif(t==7):
				y=(2.54*(10**10))*x
				print x,"in = ",y,"pm"
			elif(t==8):
				y=0.00001578283*x
				print x,"in = ",y,"mi"
			elif(t==9):
				y=0.02777777777778*x
				print x,"in = ",y,"yd"
			elif(t==10):
				y=0.08333333333333*x
				print x,"in = ",y,"ft"
			elif(t==11):
				y=x
				print x,"in = ",y,"in"
			else:
				y=2.68478212*(10**(-18))*x
				print x,"in = ",y,"ly"
	#ly to
		elif(f==12):
			if(t==1):
				y=(9.46073047*(10**12))*x
				print x,"ly = ",y,"km"
			elif(t==2):
				y=(9.46073047*(10**15))*x
				print x,"ly = ",y,"m"
			elif(t==3):
				y=(9.46073047*(10**17))*x
				print x,"ly = ",y,"cm"
			elif(t==4):
				y=(9.46073047*(10**18))*x
				print x,"ly = ",y,"mm"
			elif(t==5):
				y=(9.46073047*(10**21))*x
				print x,"ly = ",y,"micro m"
			elif(t==6):
				y=(9.46073047*(10**24))*x
				print x,"ly = ",y,"nm"
			elif(t==7):
				y=(9.46073047*(10**27))*x
				print x,"ly = ",y,"pm"
			elif(t==8):
				y=5878625380000*x
				print x,"ly = ",y,"mi"
			elif(t==9):
				y=10346380700000000*x
				print x,"ly = ",y,"yd"
			elif(t==10):
				y=31039142000000000*x
				print x,"ly = ",y,"ft"
			elif(t==11):
				y=372469704000000000*x
				print x,"ly = ",y,"in"
			else:
				y=x
				print x,"ly = ",y,"ly"
#Area
	elif(op==2):
		print "\n1.Square km\n2.Square m\n3.Square cm\n4.Square mm\n5.Hectare\n6.Acre\n7.Square Mile\n8.Square Yard\n9.Square Foot\n10.Square Inch"
		f=input("Select Unit to convert from: ")
		while(f<1 or f>10):
			f=input("Enter a valid option (1 to 10): ")
		x=input("Enter value to convert: ")
		print "\n1.Square km\n2.Square m\n3.Square cm\n4.Square mm\n5.Hectare\n6.Acre\n7.Square Mile\n8.Square Yard\n9.Square Foot\n10.Square Inch"
		t=input("Select Unit to convert to: ")
		while(t<1 or t>10):
			t=input("Enter a valid option (1 to 10): ")
	#sq km to
		if(f==1):
			if(t==1):
				y=x
				print x,"sq km = ",y,"sq km"
			elif(t==2):
				y=1000000*x
				print x,"sq km = ",y,"sq m"
			elif(t==3):
				y=10000000000*x
				print x,"sq km = ",y,"sq cm"
			elif(t==4):
				y=1000000000000*x
				print x,"sq km = ",y,"sq mm"
			elif(t==5):
				y=100*x
				print x,"sq km = ",y,"ha"
			elif(t==6):
				y=247.105407*x
				print x,"sq km = ",y,"ac"
			elif(t==7):
				y=0.386102159*x
				print x,"sq km = ",y,"sq mi"
			elif(t==8):
				y=1195990.05*x
				print x,"sq km = ",y,"sq yd"
			elif(t==9):
				y=10763910.4*x
				print x,"sq km = ",y,"sq ft"
			else:
				y=1550003100*x
				print x,"sq km = ",y,"sq in"
	#sq m to
		elif(f==2):
			if(t==1):
				y=0.000001*x
				print x,"sq m = ",y,"sq km"
			elif(t==2):
				y=x
				print x,"sq m = ",y,"sq m"
			elif(t==3):
				y=10000*x
				print x,"sq m = ",y,"sq cm"
			elif(t==4):
				y=1000000*x
				print x,"sq m = ",y,"sq mm"
			elif(t==5):
				y=0.0001*x
				print x,"sq m = ",y,"ha"
			elif(t==6):
				y=0.000247105407*x
				print x,"sq m = ",y,"ac"
			elif(t==7):
				y=0.000000386102159*x
				print x,"sq m = ",y,"sq mi"
			elif(t==8):
				y=1.19599005*x
				print x,"sq m = ",y,"sq yd"
			elif(t==9):
				y=10.7639104*x
				print x,"sq m = ",y,"sq ft"
			else:
				y=1550.0031*x
				print x,"sq m = ",y,"sq in"
	#sq cm to
		elif(f==3):
			if(t==1):
				y=0.0000000001*x
				print x,"sq cm = ",y,"sq km"
			elif(t==2):
				y=0.0001*x
				print x,"sq cm = ",y,"sq m"
			elif(t==3):
				y=x
				print x,"sq cm = ",y,"sq cm"
			elif(t==4):
				y=100*x
				print x,"sq cm = ",y,"sq mm"
			elif(t==5):
				y=0.00000001*x
				print x,"sq cm = ",y,"ha"
			elif(t==6):
				y=0.0000000247105408*x
				print x,"sq cm = ",y,"ac"
			elif(t==7):
				y=0.00000000038610216*x
				print x,"sq cm = ",y,"sq mi"
			elif(t==8):
				y=0.000119599005*x
				print x,"sq cm = ",y,"sq yd"
			elif(t==9):
				y=0.00107639104*x
				print x,"sq cm = ",y,"sq ft"
			else:
				y=0.15500031*x
				print x,"sq cm = ",y,"sq in"
	#sq mm to
		elif(f==4):
			if(t==1):
				y=0.000000000001*x
				print x,"sq mm = ",y,"sq km"
			elif(t==2):
				y=0.000001*x
				print x,"sq mm = ",y,"sq m"
			elif(t==3):
				y=0.01*x
				print x,"sq mm = ",y,"sq cm"
			elif(t==4):
				y=x
				print x,"sq mm = ",y,"sq mm"
			elif(t==5):
				y=0.0000000001*x
				print x,"sq mm = ",y,"ha"
			elif(t==6):
				y=0.000000000247105408*x
				print x,"sq mm = ",y,"ac"
			elif(t==7):
				y=0.00000000000038610216*x
				print x,"sq mm = ",y,"sq mi"
			elif(t==8):
				y=0.00000119599005*x
				print x,"sq mm = ",y,"sq yd"
			elif(t==9):
				y=0.0000107639104*x
				print x,"sq mm = ",y,"sq ft"
			else:
				y=0.0015500031*x
				print x,"sq mm = ",y,"sq in"
	#ha to
		elif(f==5):
			if(t==1):
				y=0.01*x
				print x,"ha = ",y,"sq km"
			elif(t==2):
				y=10000*x
				print x,"ha = ",y,"sq m"
			elif(t==3):
				y=100000000*x
				print x,"ha = ",y,"sq cm"
			elif(t==4):
				y=10000000000*x
				print x,"ha = ",y,"sq mm"
			elif(t==5):
				y=x
				print x,"ha = ",y,"ha"
			elif(t==6):
				y=2.47105407*x
				print x,"ha = ",y,"ac"
			elif(t==7):
				y=0.00386102159*x
				print x,"ha = ",y,"sq mi"
			elif(t==8):
				y=11959.9005*x
				print x,"ha = ",y,"sq yd"
			elif(t==9):
				y=107639.104*x
				print x,"ha = ",y,"sq ft"
			else:
				y=15500031*x
				print x,"ha = ",y,"sq in"
	#ac to
		elif(f==6):
			if(t==1):
				y=0.004046856*x
				print x,"ac = ",y,"sq km"
			elif(t==2):
				y=4046.856*x
				print x,"ac = ",y,"sq m"
			elif(t==3):
				y=40468560*x
				print x,"ac = ",y,"sq cm"
			elif(t==4):
				y=4046856000*x
				print x,"ac = ",y,"sq mm"
			elif(t==5):
				y=0.4046856*x
				print x,"ac = ",y,"ha"
			elif(t==6):
				y=x
				print x,"ac = ",y,"ac"
			elif(t==7):
				y=0.00156249984*x
				print x,"ac = ",y,"sq mi"
			elif(t==8):
				y=4839.99949*x
				print x,"ac = ",y,"sq yd"
			elif(t==9):
				y=43559.9955*x
				print x,"ac = ",y,"sq ft"
			else:
				y=6272639.35*x
				print x,"ac = ",y,"sq in"
	#mi to
		elif(f==7):
			if(t==1):
				y=2.58998811*x
				print x,"sq mi = ",y,"sq km"
			elif(t==2):
				y=2589988.11*x
				print x,"sq mi = ",y,"sq m"
			elif(t==3):
				y=25899881100*x
				print x,"sq mi = ",y,"sq cm"
			elif(t==4):
				y=2589988110000*x
				print x,"sq mi = ",y,"sq mm"
			elif(t==5):
				y=258.998811*x
				print x,"sq mi = ",y,"ha"
			elif(t==6):
				y=640.000067*x
				print x,"sq mi = ",y,"ac"
			elif(t==7):
				y=x
				print x,"sq mi = ",y,"sq mi"
			elif(t==8):
				y=3097600*x
				print x,"sq mi = ",y,"sq yd"
			elif(t==9):
				y=27878400*x
				print x,"sq mi = ",y,"sq ft"
			else:
				y=4014489600*x
				print x,"sq mi = ",y,"sq in"
	#sq yd to
		elif(f==8):
			if(t==1):
				y=0.00000083612736*x
				print x,"sq yd = ",y,"sq km"
			elif(t==2):
				y=0.83612736*x
				print x,"sq yd = ",y,"sq m"
			elif(t==3):
				y=8361.2736*x
				print x,"sq yd = ",y,"sq cm"
			elif(t==4):
				y=836127.36*x
				print x,"sq yd = ",y,"sq mm"
			elif(t==5):
				y=0.000083612736*x
				print x,"sq yd = ",y,"ha"
			elif(t==6):
				y=0.000206611592*x
				print x,"sq yd = ",y,"ac"
			elif(t==7):
				y=0.000000322830579*x
				print x,"sq yd = ",y,"sq mi"
			elif(t==8):
				y=x
				print x,"sq yd = ",y,"sq yd"
			elif(t==9):
				y=9*x
				print x,"sq yd = ",y,"sq ft"
			else:
				y=1296*x
				print x,"sq yd = ",y,"sq in"
	#sq ft to
		elif(f==9):
			if(t==1):
				y=0.00000009290304*x
				print x,"sq ft = ",y,"sq km"
			elif(t==2):
				y=0.09290304*x
				print x,"sq ft = ",y,"sq m"
			elif(t==3):
				y=929.0304*x
				print x,"sq ft = ",y,"sq cm"
			elif(t==4):
				y=92903.04*x
				print x,"sq ft = ",y,"sq mm"
			elif(t==5):
				y=0.000009290304*x
				print x,"sq ft = ",y,"ha"
			elif(t==6):
				y=0.0000229568435*x
				print x,"sq ft = ",y,"ac"
			elif(t==7):
				y=0.0000000358700643*x
				print x,"sq ft = ",y,"sq mi"
			elif(t==8):
				y=0.1111111111*x
				print x,"sq ft = ",y,"sq yd"
			elif(t==9):
				y=x
				print x,"sq ft = ",y,"sq ft"
			else:
				y=144*x
				print x,"sq ft = ",y,"sq in"
	#sq in to
		else:
			if(t==1):
				y=0.00000000064516*x
				print x,"sq in = ",y,"sq km"
			elif(t==2):
				y=0.00064516*x
				print x,"sq in = ",y,"sq m"
			elif(t==3):
				y=6.4516*x
				print x,"sq in = ",y,"sq cm"
			elif(t==4):
				y=645.16*x
				print x,"sq in = ",y,"sq mm"
			elif(t==5):
				y=0.000000064516*x
				print x,"sq in = ",y,"ha"
			elif(t==6):
				y=0.000000159422525*x
				print x,"sq in = ",y,"ac"
			elif(t==7):
				y=0.000000000249097669*x
				print x,"sq in = ",y,"sq mi"
			elif(t==8):
				y=0.000771604938*x
				print x,"sq in = ",y,"sq yd"
			elif(t==9):
				y=0.00694444445*x
				print x,"sq in = ",y,"sq ft"
			else:
				y=x
				print x,"sq in = ",y,"sq in"
#Volume
	elif(op==3):
		print "\n1.Cubic m\n2.Cubic cm\n3.Cubic mm\n4.Hectoliter\n5.Liter\n6.Milliliter\n7.Cubic ft\n8.Cubic in"
		f=input("Select Unit to convert from: ")
		while(f<1 or f>8):
			f=input("Enter a valid option (1 to 8): ")
		x=input("Enter value to convert: ")
		print "\n1.Cubic m\n2.Cubic cm\n3.Cubic mm\n4.Hectoliter\n5.Liter\n6.Milliliter\n7.Cubic ft\n8.Cubic in"
		t=input("Select Unit to convert to: ")
		while(t<1 or t>8):
			t=input("Enter a valid option (1 to 8): ")
	#cb m to
		if(f==1):
			if(t==1):
				y=x
				print x,"cubic m = ",y,"cubic m"
			elif(t==2):
				y=1000000*x
				print x,"cubic m = ",y,"cubic cm"
			elif(t==3):
				y=1000000000*x
				print x,"cubic m = ",y,"cubic mm"
			elif(t==4):
				y=10*x
				print x,"cubic m = ",y,"hl"
			elif(t==5):
				y=1000*x
				print x,"cubic m = ",y,"l"
			elif(t==6):
				y=1000000*x
				print x,"cubic m = ",y,"ml"
			elif(t==7):
				y=35.3146667*x
				print x,"cubic m = ",y,"cubic ft"
			else:
				y=61023.7441*x
				print x,"cubic m = ",y,"cubic in"
	#cb cm to
		elif(f==2):
			if(t==1):
				y=0.000001*x
				print x,"cubic cm = ",y,"cubic m"
			elif(t==2):
				y=x
				print x,"cubic cm = ",y,"cubic cm"
			elif(t==3):
				y=1000*x
				print x,"cubic cm = ",y,"cubic mm"
			elif(t==4):
				y=0.00001*x
				print x,"cubic cm = ",y,"hl"
			elif(t==5):
				y=0.001*x
				print x,"cubic cm = ",y,"l"
			elif(t==6):
				y=x
				print x,"cubic cm = ",y,"ml"
			elif(t==7):
				y=0.0000353146668*x
				print x,"cubic cm = ",y,"cubic ft"
			else:
				y=0.0610237441*x
				print x,"cubic cm = ",y,"cubic in"
	#cb mm to
		elif(f==3):
			if(t==1):
				y=0.000000001*x
				print x,"cubic mm = ",y,"cubic m"
			elif(t==2):
				y=0.001*x
				print x,"cubic mm = ",y,"cubic cm"
			elif(t==3):
				y=x
				print x,"cubic mm = ",y,"cubic mm"
			elif(t==4):
				y=0.00000001*x
				print x,"cubic mm = ",y,"hl"
			elif(t==5):
				y=0.000001*x
				print x,"cubic mm = ",y,"l"
			elif(t==6):
				y=0.001*x
				print x,"cubic mm = ",y,"ml"
			elif(t==7):
				y=0.0000000353146668*x
				print x,"cubic mm = ",y,"cubic ft"
			else:
				y=0.0000610237441*x
				print x,"cubic mm = ",y,"cubic in"
	#hl to
		elif(f==4):
			if(t==1):
				y=0.1*x
				print x,"hl = ",y,"cubic m"
			elif(t==2):
				y=100000*x
				print x,"hl = ",y,"cubic cm"
			elif(t==3):
				y=100000000*x
				print x,"hl = ",y,"cubic mm"
			elif(t==4):
				y=x
				print x,"hl = ",y,"hl"
			elif(t==5):
				y=100*x
				print x,"hl = ",y,"l"
			elif(t==6):
				y=100000*x
				print x,"hl = ",y,"ml"
			elif(t==7):
				y=3.53146668*x
				print x,"hl = ",y,"cubic ft"
			else:
				y=6102.37441*x
				print x,"hl = ",y,"cubic in"
	#l to
		elif(f==5):
			if(t==1):
				y=0.001*x
				print x,"l = ",y,"cubic m"
			elif(t==2):
				y=1000*x
				print x,"l = ",y,"cubic cm"
			elif(t==3):
				y=1000000*x
				print x,"l = ",y,"cubic mm"
			elif(t==4):
				y=0.01*x
				print x,"l = ",y,"hl"
			elif(t==5):
				y=x
				print x,"l = ",y,"l"
			elif(t==6):
				y=1000*x
				print x,"l = ",y,"ml"
			elif(t==7):
				y=0.0353146668*x
				print x,"l = ",y,"cubic ft"
			else:
				y=61.0237441*x
				print x,"l = ",y,"cubic in"
	#ml to
		elif(f==6):
			if(t==1):
				y=0.000001*x
				print x,"ml = ",y,"cubic m"
			elif(t==2):
				y=x
				print x,"ml = ",y,"cubic cm"
			elif(t==3):
				y=1000*x
				print x,"ml = ",y,"cubic mm"
			elif(t==4):
				y=0.00001*x
				print x,"ml = ",y,"hl"
			elif(t==5):
				y=0.001*x
				print x,"ml = ",y,"l"
			elif(t==6):
				y=x
				print x,"ml = ",y,"ml"
			elif(t==7):
				y=0.0000353146668*x
				print x,"ml = ",y,"cubic ft"
			else:
				y=0.0610237441*x
				print x,"ml = ",y,"cubic in"
	#cb ft to
		elif(f==7):
			if(t==1):
				y=0.0283168466*x
				print x,"cb ft = ",y,"cubic m"
			elif(t==2):
				y=28316.8466*x
				print x,"cb ft = ",y,"cubic cm"
			elif(t==3):
				y=28316846.6*x
				print x,"cb ft = ",y,"cubic mm"
			elif(t==4):
				y=0.283168466*x
				print x,"cb ft = ",y,"hl"
			elif(t==5):
				y=28.3168466*x
				print x,"cb ft = ",y,"l"
			elif(t==6):
				y=28316.8466*x
				print x,"cb ft = ",y,"ml"
			elif(t==7):
				y=x
				print x,"cb ft = ",y,"cubic ft"
			else:
				y=1728*x
				print x,"cb ft = ",y,"cubic in"
	#cb in to
		else:
			if(t==1):
				y=0.000016387064*x
				print x,"cb in = ",y,"cubic m"
			elif(t==2):
				y=16.387064*x
				print x,"cb in = ",y,"cubic cm"
			elif(t==3):
				y=16387.064*x
				print x,"cb in = ",y,"cubic mm"
			elif(t==4):
				y=0.00016387064*x
				print x,"cb in = ",y,"hl"
			elif(t==5):
				y=0.016387064*x
				print x,"cb in = ",y,"l"
			elif(t==6):
				y=16.387064*x
				print x,"cb in = ",y,"ml"
			elif(t==7):
				y=0.000578703704*x
				print x,"cb in = ",y,"cubic ft"
			else:
				y=x
				print x,"cb in = ",y,"cubic in"
#Temp
	elif(op==4):
		print "\n1.Celsius\n2.Fahrenheit\n3.Kelvin"
		f=input("Select Unit to convert from: ")
		while(f<1 or f>3):
			f=input("Enter a valid option (1 to 3): ")
		x=input("Enter value to convert: ")
		print "\n1.Celsius\n2.Fahrenheit\n3.Kelvin"
		t=input("Select Unit to convert to: ")
		while(t<1 or t>3):
			t=input("Enter a valid option (1 to 3): ")
	#C to
		if(f==1):
			if(t==1):
				y=x
				print x,"Celsius = ",y,"Celsius"
			elif(t==2):
				y=(x*(9.0/5))+32
				print x,"Celsius = ",y,"Fahrenheit"
			else:
				y=x+273.15
				print x,"Celsius = ",y,"Kelvin"
	#F to
		elif(f==2):
			if(t==1):
				y=(x-32)*(5.0/9)
				print x,"Fahrenheit = ",y,"Celsius"
			elif(t==2):
				y=x
				print x,"Fahrenheit = ",y,"Fahrenheit"
			else:
				y=(x-32)*(5.0/9)+273.15
				print x,"Fahrenheit = ",y,"Kelvin"
	#K to
		else:
			if(t==1):
				y=x-273.15
				print x,"Kelvin = ",y,"Celsius"
			elif(t==2):
				y=(x-273.15)*(9.0/5)+32
				print x,"Kelvin = ",y,"Fahrenheit"
			else:
				y=x
				print x,"Kelvin = ",y,"Kelvin"
#Speed
	elif(op==5):
		print "\n1.Light Speed(c)\n2.Mach(Ma)\n3.Meter/Second(mps)\n4.Kilometer/Hour(kmph)\n5.Knot(kn)\n6.Mile/Hour(mph)"
		f=input("Select Unit to convert from: ")
		while(f<1 or f>6):
			f=input("Enter a valid option (1 to 6): ")
		x=input("Enter value to convert: ")
		print "\n1.Light Speed(c)\n2.Mach(Ma)\n3.Meter/Second(mps)\n4.Kilometer/Hour(kmph)\n5.Knot(kn)\n6.Mile/Hour(mph)"
		t=input("Select Unit to convert to: ")
		while(t<1 or t>6):
			t=input("Enter a valid option (1 to 6): ")
	#lightspeed to
		if(f==1):
			if(t==1):
				y=x
				print x,"C = ",y,"c"
			elif(t==2):
				y=880965.201*x
				print x,"C = ",y,"Ma"
			elif(t==3):
				y=299792458*x
				print x,"C = ",y,"mps"
			elif(t==4):
				y=1079252850*x
				print x,"C = ",y,"kmph"
			elif(t==5):
				y=582749918*x
				print x,"C = ",y,"kn"
			else:
				y=670616629*x
				print x,"C = ",y,"mph"
	#mach to
		elif(f==2):
			if(t==1):
				y=x*0.00000113511862
				print x,"Ma = ",y,"c"
			elif(t==2):
				y=x
				print x,"Ma= ",y,"Ma"
			elif(t==3):
				y=340.3*x
				print x,"Ma = ",y,"mps"
			elif(t==4):
				y=1225.08*x
				print x,"Ma = ",y,"kmph"
			elif(t==5):
				y=661.490281*x
				print x,"Ma = ",y,"kn"
			else:
				y=761.22942*x
				print x,"Ma = ",y,"mph"
	#mps to
		elif(f==3):
			if(t==1):
				y=0.0000000033564095*x
				print x,"mps = ",y,"c"
			elif(t==2):
				y=0.0029385836*x
				print x,"mps = ",y,"Ma"
			elif(t==3):
				y=x
				print x,"mps = ",y,"mps"
			elif(t==4):
				y=3.6*x
				print x,"mps = ",y,"kmph"
			elif(t==5):
				y=1.94384449*x
				print x,"mps = ",y,"kn"
			else:
				y=2.3693629*x
				print x,"mps = ",y,"mph"
	#kmph to
		elif(f==4):
			if(t==1):
				y=0.000000000926566931*x
				print x,"kmph = ",y,"c"
			elif(t==2):
				y=0.000816273223
				print x,"kmph = ",y,"Ma"
			elif(t==3):
				y=0.27777777777778*x
				print x,"kmph = ",y,"mps"
			elif(t==4):
				y=x
				print x,"kmph = ",y,"kmph"
			elif(t==5):
				y=0.539956803*x
				print x,"kmph = ",y,"kn"
			else:
				y=0.621371192*x
				print x,"kmph = ",y,"mph"
	#knot to
		elif(f==5):
			if(t==1):
				y=0.00000000171600196*x
				print x,"kn = ",y,"c"
			elif(t==2):
				y=0.00151173801*x
				print x,"kn = ",y,"Ma"
			elif(t==3):
				y=0.5144444444444
				print x,"kn = ",y,"mps"
			elif(t==4):
				y=1.852*x
				print x,"kn = ",y,"kmph"
			elif(t==5):
				y=x
				print x,"kn = ",y,"kn"
			else:
				y=1.15077945*x
				print x,"kn = ",y,"mph"
	#mph to
		else:
			if(t==1):
				y=0.000000001491164934*x
				print x,"mph = ",y,"c"
			elif(t==2):
				y=0.0013136641*x
				print x,"mph = ",y,"Ma"
			elif(t==3):
				y=0.44704*x
				print x,"mph = ",y,"mps"
			elif(t==4):
				y=1.609344*x
				print x,"mph = ",y,"kmph"
			elif(t==5):
				y=0.868976242*x
				print x,"mph = ",y,"kn"
			else:
				y=x
				print x,"mph = ",y,"mph"
#Time
	elif(op==6):
		print "\n1.Seconds\n2.Minutes\n3.Hours\n4.Days\n5.Week\n6.Year"
		f=input("Select Unit to convert from: ")
		while(f<1 or f>6):
			f=input("Enter a valid option (1 to 6): ")
		x=input("Enter value to convert: ")
		print "\n1.Seconds\n2.Minutes\n3.Hours\n4.Days\n5.Week\n6.Year"
		t=input("Select Unit to convert to: ")
		while(t<1 or t>6):
			t=input("Enter a valid option (1 to 6): ")
	#sec to
		if(f==1):
			if(t==1):
				y=x
				print x,"s = ",y,"s"
			elif(t==2):
				y=0.016666666666667*x
				print x,"s = ",y,"min"
			elif(t==3):
				y=0.000277777777778*x
				print x,"s = ",y,"hrs"
			elif(t==4):
				y=0.0000115740741*x
				print x,"s = ",y,"days"
			elif(t==5):
				y=0.00000165343915*x
				print x,"s = ",y,"wks"
			else:
				y=0.000000031709792*x
				print x,"s = ",y,"yrs"
	#min to
		elif(f==2):
			if(t==1):
				y=60*x
				print x,"min = ",y,"s"
			elif(t==2):
				y=x
				print x,"min = ",y,"min"
			elif(t==3):
				y=0.0166666666666667*x
				print x,"min = ",y,"hrs"
			elif(t==4):
				y=0.0006944444444444*x
				print x,"min = ",y,"days"
			elif(t==5):
				y=0.0000992063492*x
				print x,"min = ",y,"wks"
			else:
				y=0.00000190258752*x
				print x,"min = ",y,"yrs"
	#hrs to
		elif(f==3):
			if(t==1):
				y=3600*x
				print x,"hrs = ",y,"s"
			elif(t==2):
				y=60*x
				print x,"hrs = ",y,"min"
			elif(t==3):
				y=x
				print x,"hrs = ",y,"hrs"
			elif(t==4):
				y=0.04166666666667*x
				print x,"hrs = ",y,"days"
			elif(t==5):
				y=0.00595238095*x
				print x,"hrs = ",y,"wks"
			else:
				y=0.000114155251*x
				print x,"hrs = ",y,"yrs"
	#days to
		elif(f==4):
			if(t==1):
				y=86400*x
				print x,"days = ",y,"s"
			elif(t==2):
				y=1440*x
				print x,"days = ",y,"min"
			elif(t==3):
				y=24
				print x,"days = ",y,"hrs"
			elif(t==4):
				y=x
				print x,"days = ",y,"days"
			elif(t==5):
				y=0.142857143*x
				print x,"days = ",y,"wks"
			else:
				y=0.00273972603*x
				print x,"days = ",y,"yrs"
	#weeks to
		elif(f==5):
			if(t==1):
				y=604800*x
				print x,"wks = ",y,"s"
			elif(t==2):
				y=10080*x
				print x,"wks = ",y,"min"
			elif(t==3):
				y=168*x
				print x,"wks = ",y,"hrs"
			elif(t==4):
				y=7*x
				print x,"wks = ",y,"days"
			elif(t==5):
				y=x
				print x,"wks = ",y,"wks"
			else:
				y=0.0191780822*x
				print x,"wks = ",y,"yrs"
	#yrs to
		else:
			if(t==1):
				y=31536000*x
				print x,"yrs = ",y,"s"
			elif(t==2):
				y=525600*x
				print x,"yrs = ",y,"min"
			elif(t==3):
				y=8760*x
				print x,"yrs = ",y,"hrs"
			elif(t==4):
				y=365*x
				print x,"yrs = ",y,"days"
			elif(t==5):
				y=52.142857*x
				print x,"yrs = ",y,"wks"
			else:
				y=x
				print x,"yrs = ",y,"yrs"
#Mass
	else:
		print "\n1.Tonne(t)\n2.Kilogram(kg)\n3.Gram(g)\n4.Milligram(mg)\n5.Quintal(q)\n6.Pound(lb)\n7.Ounce(oz)"
		f=input("Select Unit to convert from: ")
		while(f<1 or f>7):
			f=input("Enter a valid option (1 to 7): ")
		x=input("Enter value to convert: ")
		print "\n1.Tonne(t)\n2.Kilogram(kg)\n3.Gram(g)\n4.Milligram(mg)\n5.Quintal(q)\n6.Pound(lb)\n7.Ounce(oz)"
		t=input("Select Unit to convert to: ")
		while(t<1 or t>7):
			t=input("Enter a valid option (1 to 7): ")
	#tonne to
		if(f==1):
			if(t==1):
				y=x
				print x,"t = ",y,"t"
			elif(t==2):
				y=1000*x
				print x,"t = ",y,"kg"
			elif(t==3):
				y=1000000*x
				print x,"s = ",y,"g"
			elif(t==4):
				y=1000000000*x
				print x,"t = ",y,"mg"
			elif(t==5):
				y=10*x
				print x,"t = ",y,"q"
			elif(t==6):
				y=2204.62262*x
				print x,"t = ",y,"lb"
			else:
				y=35273.9619*x
				print x,"t = ",y,"oz"
	#kg to
		elif(f==2):
			if(t==1):
				y=0.001*x
				print x,"kg = ",y,"t"
			elif(t==2):
				y=x
				print x,"kg = ",y,"kg"
			elif(t==3):
				y=1000*x
				print x,"kg = ",y,"g"
			elif(t==4):
				y=1000000*x
				print x,"kg = ",y,"mg"
			elif(t==5):
				y=0.01
				print x,"kg = ",y,"q"
			elif(t==6):
				y=2.20462262*x
				print x,"kg = ",y,"lb"
			else:
				y=35.2739619*x
				print x,"kg = ",y,"oz"
	#g to
		elif(f==3):
			if(t==1):
				y=0.000001*x
				print x,"g = ",y,"t"
			elif(t==2):
				y=0.001*x
				print x,"g = ",y,"kg"
			elif(t==3):
				y=x
				print x,"g = ",y,"g"
			elif(t==4):
				y=1000*x
				print x,"g = ",y,"mg"
			elif(t==5):
				y=0.00001*x
				print x,"g = ",y,"q"
			elif(t==6):
				y=0.00220462262*x
				print x,"g = ",y,"lb"
			else:
				y=0.0352739619*x
				print x,"g = ",y,"oz"
	#mg to
		elif(f==4):
			if(t==1):
				y=0.000000001*x
				print x,"mg = ",y,"t"
			elif(t==2):
				y=0.000001*x
				print x,"mg = ",y,"kg"
			elif(t==3):
				y=0.001*x
				print x,"mg = ",y,"g"
			elif(t==4):
				y=x
				print x,"mg = ",y,"mg"
			elif(t==5):
				y=0.00000001*x
				print x,"mg = ",y,"q"
			elif(t==6):
				y=0.00000220462262*x
				print x,"mg = ",y,"lb"
			else:
				y=0.0000352739619*x
				print x,"mg = ",y,"oz"
	#quintal to
		elif(f==5):
			if(t==1):
				y=0.1*x
				print x,"q = ",y,"t"
			elif(t==2):
				y=100*x
				print x,"q = ",y,"kg"
			elif(t==3):
				y=100000*x
				print x,"q = ",y,"g"
			elif(t==4):
				y=100000000*x
				print x,"q = ",y,"mg"
			elif(t==5):
				y=x
				print x,"q = ",y,"q"
			elif(t==6):
				y=220.462262*x
				print x,"q = ",y,"lb"
			else:
				y=3527.39619*x
				print x,"q = ",y,"oz"
	#pound to
		elif(f==6):
			if(t==1):
				y=0.0004535937*x
				print x,"lb = ",y,"t"
			elif(t==2):
				y=0.4535937*x
				print x,"lb = ",y,"kg"
			elif(t==3):
				y=453.59237*x
				print x,"lb = ",y,"g"
			elif(t==4):
				y=453592.37*x
				print x,"lb = ",y,"mg"
			elif(t==5):
				y=0.0045359237*x
				print x,"lb = ",y,"q"
			elif(t==6):
				y=x
				print x,"lb = ",y,"lb"
			else:
				y=16*x
				print x,"lb = ",y,"oz"
	#ounce to
		else:
			if(t==1):
				y=0.0000283495231*x
				print x,"oz = ",y,"t"
			elif(t==2):
				y=0.0283495231*x
				print x,"oz = ",y,"kg"
			elif(t==3):
				y=28.3495231*x
				print x,"oz = ",y,"g"
			elif(t==4):
				y=28349.5231*x
				print x,"oz = ",y,"mg"
			elif(t==5):
				y=0.000283495231*x
				print x,"oz = ",y,"q"
			elif(t==6):
				y=0.0625*x
				print x,"oz = ",y,"lb"
			else:
				y=x
				print x,"oz = ",y,"oz"

#Exit Sequence
	exit=raw_input( "\nDo you want to exit?(Y/N) : ")
	exit=exit.upper()
	if (exit=="Y"):
		print "\n\t\t\t\t\t\t\t*************\n\t\t\t\t\t\t\t|  GOODBYE  |\n\t\t\t\t\t\t\t*************\n\n\n"
		break
	if (exit=="N"):
		print"\nGoodLuck\n"
		continue
	if(exit!="N" or exit!="Y"):
		while(1):
			exit=raw_input("Enter a valid option : (Y/N) ")
			exit=exit.upper()
			if(exit=="Y" or exit=="N"):
				break
		if (exit=="N"):
			print"\nGoodLuck\n"
			continue
		if (exit=="Y"):
			print "\n\t\t\t\t\t\t\t*************\n\t\t\t\t\t\t\t|  GOODBYE  |\n\t\t\t\t\t\t\t*************\n\n\n"
			break
	break
