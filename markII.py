from tkinter import *
from tkinter import messagebox

window=Tk()
window.title('Unit Converter')
window.geometry('750x450')
window.resizable(0,0)
menubar=Menu(window,bg='#505050',activebackground='#000000',activeforeground='#ffffff')
window.config(menu=menubar,bg='#101010')

def fnHome():
	try:
		frameList.destroy()
	except:
		None
	homeFrame=Frame(window,height=300,width=350,bg='#101010')
	homeFrame.place(x=200,y=55)
	btnLen=Button(homeFrame,text='Length',relief='raised',bd=5,font=('bold',12),height=3,width=7,bg='#ff55ff',activebackground='#dd25dd',padx=1,pady=0,command=lambda:fnUnits('len')).place(x=135,y=15)
	btnArea=Button(homeFrame,text='Area',relief='raised',bd=3,font=('bold',12),height=3,width=7,bg='#ee7755',activebackground='#ff7725',padx=1,pady=0,command=lambda:fnUnits('area')).place(x=5,y=75)
	btnVol=Button(homeFrame,text='Volume',relief='raised',bd=3,font=('bold',12),height=3,width=7,bg='#55cc55',activebackground='#25aa25',padx=1,pady=0,command=lambda:fnUnits('vol')).place(x=260,y=75)
	btnMass=Button(homeFrame,text='Mass',relief='raised',bd=3,font=('bold',12),height=3,width=7,bg='#9955ff',activebackground='#8825dd',padx=1,pady=0,command=lambda:fnUnits('mass')).place(x=5,y=175)
	btnTemp=Button(homeFrame,text='Heat',relief='raised',bd=3,font=('bold',12),height=3,width=7,bg='#ff5555',activebackground='#ee2525',padx=1,pady=0,command=lambda:fnUnits('temp')).place(x=260,y=175)
	btnSpeed=Button(homeFrame,text='Speed',relief='raised',bd=3,font=('bold',12),height=3,width=7,bg='#ffdd25',activebackground='#ffaa25',padx=1,pady=0,command=lambda:fnUnits('speed')).place(x=135,y=230)
	btnTime=Button(homeFrame,text='Time',relief='raised',bd=3,font=('bold',12),height=3,width=7,bg='#5599ff',activebackground='#2555ee',padx=1,pady=0,command=lambda:fnUnits('time')).place(x=135,y=125)
def fnUnits(op):
	global frameList,varFrom,varTo,txtFrom,txtTo
	frameList=Frame(window,bg='#101010',height=300,width=500)
	frameList.place(x=175,y=55)
	len=['Kilometer(Km)','Meter(m)','Centimter(cm)','Millimeter(mm)','Micrometer('+chr(181)+'m)','Nanometer(nm)','Picometer(pm)','Mile(mi)','Yard(yd)','Foot(ft)','Inch(in)','Light Year(ly)']
	area=['Square Km(Km'+chr(178)+')','Square Meter(m'+chr(178)+')','Square cm(cm'+chr(178)+')','Square mm(mm'+chr(178)+')','Hectare','Acre','Square Mile(mi'+chr(178)+')','Square Yard(yd'+chr(178)+')','Square Foot(ft'+chr(178)+')','Square Inch(in'+chr(178)+')']
	vol=['Cubic Meter(m'+chr(179)+')','Cubic cm(cm'+chr(179)+')','Cubic mm(mm'+chr(179)+')','Hectoliter','Liter','Milliliter','Cubic Feet(ft'+chr(179)+')','Cubic Inch(in'+chr(179)+')']
	mass=['Tonne(t)','Kilogram(Kg)','Gram(g)','Milligram(mg)','Quintal(q)','Pound(lb)','Ounce(oz)']
	temp=['Celsius('+chr(176)+'C)','Farenheit('+chr(176)+'F)','Kelvin(K)']
	speed=['Light Speed(C)','Mach(Ma)','Meter/Speed(mps)','Kilometer/Hour(Kmph)','Knot(kn)','Miles/Hour(mph)']
	time=['Seconds','Minutes','Hour','Days','Weeks','Year']
	if(op=='len'):
		list=len
	elif(op=='area'):
		list=area
	elif(op=='vol'):
		list=vol
	elif(op=='mass'):
		list=mass
	elif(op=='temp'):
		list=temp
	elif(op=='speed'):
		list=speed
	else:
		list=time
	varFrom=StringVar()
	varFrom.set('From')
	varTo=StringVar()
	varTo.set('To')
	dropFrom=OptionMenu(frameList,varFrom,*list)
	dropFrom.config(bg='#101010',fg='#ffffff',activeforeground='#ffffff',activebackground='#505050',bd=0)
	dropFrom['menu'].config(bg='#666666',activebackground='#080808',activeforeground='#ffffff')
	dropFrom.place(x=0,y=50)
	txtFrom=Entry(frameList,width=10)
	txtFrom.place(x=0,y=100)
	dropTo=OptionMenu(frameList,varTo,*list)
	dropTo.config(bg='#101010',fg='#ffffff',activeforeground='#ffffff',activebackground='#505050',bd=0)
	dropTo['menu'].config(bg='#666666',activebackground='#080808',activeforeground='#ffffff')
	dropTo.place(x=312,y=50)
	txtTo=Entry(frameList,width=10)
	txtTo.place(x=312,y=100)
	btnConvert=Button(frameList,text='Convert',bg='#000000',fg='#ffffff',activebackground='#000000',activeforeground='#ffffff',command=lambda:fnConvert(op)).place(x=175,y=150)
def fnConvert(op):
	txtTo.delete(0,END)
	From=varFrom.get()
	To=varTo.get()
	if(From=='From' or To=='To'):
		messagebox.showwarning(message='Select Both Units')
		return
	else:
		try:
			x=float(txtFrom.get())
		except:
			messagebox.showwarning(message='Invalid Input')
			return
		if(op=='len'):
			if(From=='Kilometer(Km)'):
				if(To=='Kilometer(Km)'):
					y=x
				elif(To=='Meter(m)'):
					y=x*1000
				elif(To=='Centimter(cm)'):
					y=x*100000
				elif(To=='Millimeter(mm)'):
					y=x*1000000
				elif(To=='Micrometer('+chr(181)+'m)'):
					y=x*100000000
				elif(To=='Nanometer(nm)'):
					y=x*100000000000
				elif(To=='Picometer(pm)'):
					y=x*100000000000000
				elif(To=='Mile(mi)'):
					y=x*0.621371192
				elif(To=='Yard(yd)'):
					y=x*1093.6133
				elif(To=='Foot(ft)'):
					y=x*3280.8399
				elif(To=='Inch(in)'):
					y=x*39370.0787
				else:
					y=x*1.057*(10**(-13))
			elif(From=='Meter(m)'):
				if(To=='Kilometer(Km)'):
					y=x*0.001
				elif(To=='Meter(m)'):
					y=x
				elif(To=='Centimter(cm)'):
					y=x*100
				elif(To=='Millimeter(mm)'):
					y=x*1000
				elif(To=='Micrometer('+chr(181)+'m)'):
					y=x*1000000
				elif(To=='Nanometer(nm)'):
					y=x*1000000000
				elif(To=='Picometer(pm)'):
					y=x*1000000000000
				elif(To=='Mile(mi)'):
					y=x*0.000621371192
				elif(To=='Yard(yd)'):
					y=x*1.0936133
				elif(To=='Foot(ft)'):
					y=x*3.2808399
				elif(To=='Inch(in)'):
					y=x*39.3700787
				else:
					y=x*1.057*(10**(-16))
			elif(From=='Centimter(cm)'):
				if(To=='Kilometer(Km)'):
					y=x*0.00001
				elif(To=='Meter(m)'):
					y=x*0.01
				elif(To=='Centimter(cm)'):
					y=x
				elif(To=='Millimeter(mm)'):
					y=x*10
				elif(To=='Micrometer('+chr(181)+'m)'):
					y=x*10000
				elif(To=='Nanometer(nm)'):
					y=x*10000000
				elif(To=='Picometer(pm)'):
					y=x*10000000000
				elif(To=='Mile(mi)'):
					y=x*0.00000621371192
				elif(To=='Yard(yd)'):
					y=x*0.010936133
				elif(To=='Foot(ft)'):
					y=x*0.032808399
				elif(To=='Inch(in)'):
					y=x*0.393700787
				else:
					y=x*1.057*(10**(-18))
			elif(From=='Millimeter(mm)'):
				if(To=='Kilometer(Km)'):
					y=x*0.000001
				elif(To=='Meter(m)'):
					y=x*0.001
				elif(To=='Centimter(cm)'):
					y=x*0.1
				elif(To=='Millimeter(mm)'):
					y=x
				elif(To=='Micrometer('+chr(181)+'m)'):
					y=x*1000
				elif(To=='Nanometer(nm)'):
					y=x*1000000
				elif(To=='Picometer(pm)'):
					y=x*1000000000
				elif(To=='Mile(mi)'):
					y=x*0.000000621371192
				elif(To=='Yard(yd)'):
					y=x*0.0010936133
				elif(To=='Foot(ft)'):
					y=x*0.0032808399
				elif(To=='Inch(in)'):
					y=x*0.0393700787
				else:
					y=x*1.057*(10**(-19))
			elif(From=='Micrometer('+chr(181)+'m)'):
				if(To=='Kilometer(Km)'):
					y=x*0.000000001
				elif(To=='Meter(m)'):
					y=x*0.000001
				elif(To=='Centimter(cm)'):
					y=x*0.0001
				elif(To=='Millimeter(mm)'):
					y=x*0.001
				elif(To=='Micrometer('+chr(181)+'m)'):
					y=x
				elif(To=='Nanometer(nm)'):
					y=x*1000
				elif(To=='Picometer(pm)'):
					y=x*1000000
				elif(To=='Mile(mi)'):
					y=x*0.000000000621371192
				elif(To=='Yard(yd)'):
					y=x*0.0000010936133
				elif(To=='Foot(ft)'):
					y=x*0.0000032808399
				elif(To=='Inch(in)'):
					y=x*0.0000393700787
				else:
					y=x*1.057*(10**(-22))
			elif(From=='Nanometer(nm)'):
				if(To=='Kilometer(Km)'):
					y=x*0.000000000001
				elif(To=='Meter(m)'):
					y=x*0.000000001
				elif(To=='Centimter(cm)'):
					y=x*0.0000001
				elif(To=='Millimeter(mm)'):
					y=x*0.000001
				elif(To=='Micrometer('+chr(181)+'m)'):
					y=x*0.001
				elif(To=='Nanometer(nm)'):
					y=x
				elif(To=='Picometer(pm)'):
					y=x*1000
				elif(To=='Mile(mi)'):
					y=x*0.000000000000621371192
				elif(To=='Yard(yd)'):
					y=x*0.0000000010936133
				elif(To=='Foot(ft)'):
					y=x*0.0000000032808399
				elif(To=='Inch(in)'):
					y=x*0.0000000393700787
				else:
					y=x*1.057*(10**(-25))
			elif(From=='Picometer(pm)'):
				if(To=='Kilometer(Km)'):
					y=x*0.000000000000001
				elif(To=='Meter(m)'):
					y=x*0.000000000001
				elif(To=='Centimter(cm)'):
					y=x*0.0000000001
				elif(To=='Millimeter(mm)'):
					y=x*0.000000001
				elif(To=='Micrometer('+chr(181)+'m)'):
					y=x*0.000001
				elif(To=='Nanometer(nm)'):
					y=x*0.001
				elif(To=='Picometer(pm)'):
					y=x
				elif(To=='Mile(mi)'):
					y=x*0.000000000000000621371192
				elif(To=='Yard(yd)'):
					y=x*0.0000000000010936133
				elif(To=='Foot(ft)'):
					y=x*0.0000000000032808399
				elif(To=='Inch(in)'):
					y=x*0.0000000000393700787
				else:
					y=x*1.057*(10**(-28))
			elif(From=='Mile(mi)'):
				if(To=='Kilometer(Km)'):
					y=x*1.609344
				elif(To=='Meter(m)'):
					y=x*1609.344
				elif(To=='Centimter(cm)'):
					y=x*160934.4
				elif(To=='Millimeter(mm)'):
					y=x*1609344
				elif(To=='Micrometer('+chr(181)+'m)'):
					y=x*1609344000
				elif(To=='Nanometer(nm)'):
					y=x*1609344000000
				elif(To=='Picometer(pm)'):
					y=x*1609344000000000
				elif(To=='Mile(mi)'):
					y=x
				elif(To=='Yard(yd)'):
					y=x*1760
				elif(To=='Foot(ft)'):
					y=x*5280
				elif(To=='Inch(in)'):
					y=x*63360
				else:
					y=x*1.70107795*(10**(-13))
			elif(From=='Yard(yd)'):
				if(To=='Kilometer(Km)'):
					y=x*0.0009144
				elif(To=='Meter(m)'):
					y=x*0.9144
				elif(To=='Centimter(cm)'):
					y=x*91.44
				elif(To=='Millimeter(mm)'):
					y=x*914.4
				elif(To=='Micrometer('+chr(181)+'m)'):
					y=x*914400
				elif(To=='Nanometer(nm)'):
					y=x*914400000
				elif(To=='Picometer(pm)'):
					y=x*914400000000
				elif(To=='Mile(mi)'):
					y=x*0.000568181818
				elif(To=='Yard(yd)'):
					y=x
				elif(To=='Foot(ft)'):
					y=x*3
				elif(To=='Inch(in)'):
					y=x*36
				else:
					y=x*9.66521563*(10**(-17))
			elif(From=='Foot(ft)'):
				if(To=='Kilometer(Km)'):
					y=x*0.0003048
				elif(To=='Meter(m)'):
					y=x*0.3048
				elif(To=='Centimter(cm)'):
					y=x*30.48
				elif(To=='Millimeter(mm)'):
					y=x*304.8
				elif(To=='Micrometer('+chr(181)+'m)'):
					y=x*304800
				elif(To=='Nanometer(nm)'):
					y=x*304800000
				elif(To=='Picometer(pm)'):
					y=x*(3.048*(10**11))
				elif(To=='Mile(mi)'):
					y=x*0.000189393939
				elif(To=='Yard(yd)'):
					y=x*0.33333333333333
				elif(To=='Foot(ft)'):
					y=x
				elif(To=='Inch(in)'):
					y=x*12
				else:
					y=x*3.22173854*(10**(-17))
			elif(From=='Inch(in)'):
				if(To=='Kilometer(Km)'):
					y=x*0.0000254
				elif(To=='Meter(m)'):
					y=x*0.0254
				elif(To=='Centimter(cm)'):
					y=x*2.54
				elif(To=='Millimeter(mm)'):
					y=x*25.4
				elif(To=='Micrometer('+chr(181)+'m)'):
					y=x*25400
				elif(To=='Nanometer(nm)'):
					y=x*25400000
				elif(To=='Picometer(pm)'):
					y=x*(2.54*(10**10))
				elif(To=='Mile(mi)'):
					y=x*0.00001578283
				elif(To=='Yard(yd)'):
					y=x*0.02777777777778
				elif(To=='Foot(ft)'):
					y=x*0.08333333333333
				elif(To=='Inch(in)'):
					y=x
				else:
					y=x*2.68478212*(10**(-18))
			else:
				if(To=='Kilometer(Km)'):
					y=x*(9.46073047*(10**12))
				elif(To=='Meter(m)'):
					y=x*(9.46073047*(10**15))
				elif(To=='Centimter(cm)'):
					y=x*(9.46073047*(10**17))
				elif(To=='Millimeter(mm)'):
					y=x*(9.46073047*(10**18))
				elif(To=='Micrometer('+chr(181)+'m)'):
					y=x*(9.46073047*(10**21))
				elif(To=='Nanometer(nm)'):
					y=x*(9.46073047*(10**24))
				elif(To=='Picometer(pm)'):
					y=x*(9.46073047*(10**27))
				elif(To=='Mile(mi)'):
					y=x*5878625380000
				elif(To=='Yard(yd)'):
					y=x*10346380700000000
				elif(To=='Foot(ft)'):
					y=x*31039142000000000
				elif(To=='Inch(in)'):
					y=x*372469704000000000
				else:
					y=x
		elif(op=='area'):
			if(From=='Square Km(Km'+chr(178)+')'):
				if(To=='Square Km(Km'+chr(178)+')'):
					y=x
				elif(To=='Square Meter(m'+chr(178)+')'):
					y=x*1000000
				elif(To=='Square cm(cm'+chr(178)+')'):
					y=x*10000000000
				elif(To=='Square mm(mm'+chr(178)+')'):
					y=x*1000000000000
				elif(To=='Hectare'):
					y=x*100
				elif(To=='Acre'):
					y=x*247.105407
				elif(To=='Square Mile(mi'+chr(178)+')'):
					y=x*0.386102159
				elif(To=='Square Yard(yd'+chr(178)+')'):
					y=x*1195990.05
				elif(To=='Square Foot(ft'+chr(178)+')'):
					y=x*10763910.4
				else:
					y=x*1550003100
			elif(From=='Square Meter(m'+chr(178)+')'):
				if(To=='Square Km(Km'+chr(178)+')'):
					y=x*0.000001
				elif(To=='Square Meter(m'+chr(178)+')'):
					y=x
				elif(To=='Square cm(cm'+chr(178)+')'):
					y=x*10000
				elif(To=='Square mm(mm'+chr(178)+')'):
					y=x*1000000
				elif(To=='Hectare'):
					y=x*0.0001
				elif(To=='Acre'):
					y=x*0.000247105407
				elif(To=='Square Mile(mi'+chr(178)+')'):
					y=x*0.000000386102159
				elif(To=='Square Yard(yd'+chr(178)+')'):
					y=x*1.19599005
				elif(To=='Square Foot(ft'+chr(178)+')'):
					y=x*10.7639104
				else:
					y=x*1550.0031
			elif(From=='Square cm(cm'+chr(178)+')'):
				if(To=='Square Km(Km'+chr(178)+')'):
					y=x*0.0000000001
				elif(To=='Square Meter(m'+chr(178)+')'):
					y=x*0.0001
				elif(To=='Square cm(cm'+chr(178)+')'):
					y=x
				elif(To=='Square mm(mm'+chr(178)+')'):
					y=x*100
				elif(To=='Hectare'):
					y=x*0.00000001
				elif(To=='Acre'):
					y=x*0.0000000247105408
				elif(To=='Square Mile(mi'+chr(178)+')'):
					y=x*0.00000000038610216
				elif(To=='Square Yard(yd'+chr(178)+')'):
					y=x*0.000119599005
				elif(To=='Square Foot(ft'+chr(178)+')'):
					y=x*0.00107639104
				else:
					y=x*0.15500031
			elif(From=='Square mm(mm'+chr(178)+')'):
				if(To=='Square Km(Km'+chr(178)+')'):
					y=x*0.000000000001
				elif(To=='Square Meter(m'+chr(178)+')'):
					y=x*0.000001
				elif(To=='Square cm(cm'+chr(178)+')'):
					y=x*0.01
				elif(To=='Square mm(mm'+chr(178)+')'):
					y=x
				elif(To=='Hectare'):
					y=x*0.0000000001
				elif(To=='Acre'):
					y=x*0.000000000247105408
				elif(To=='Square Mile(mi'+chr(178)+')'):
					y=x*0.00000000000038610216
				elif(To=='Square Yard(yd'+chr(178)+')'):
					y=x*0.00000119599005
				elif(To=='Square Foot(ft'+chr(178)+')'):
					y=x*0.0000107639104
				else:
					y=x*0.0015500031
			elif(From=='Hectare'):
				if(To=='Square Km(Km'+chr(178)+')'):
					y=x*0.01
				elif(To=='Square Meter(m'+chr(178)+')'):
					y=x*10000
				elif(To=='Square cm(cm'+chr(178)+')'):
					y=x*100000000
				elif(To=='Square mm(mm'+chr(178)+')'):
					y=x*10000000000
				elif(To=='Hectare'):
					y=x
				elif(To=='Acre'):
					y=x*2.47105407
				elif(To=='Square Mile(mi'+chr(178)+')'):
					y=x*0.00386102159
				elif(To=='Square Yard(yd'+chr(178)+')'):
					y=x*11959.9005
				elif(To=='Square Foot(ft'+chr(178)+')'):
					y=x*107639.104
				else:
					y=x*15500031
			elif(From=='Acre'):
				if(To=='Square Km(Km'+chr(178)+')'):
					y=x*0.004046856
				elif(To=='Square Meter(m'+chr(178)+')'):
					y=x*4046.856
				elif(To=='Square cm(cm'+chr(178)+')'):
					y=x*40468560
				elif(To=='Square mm(mm'+chr(178)+')'):
					y=x*4046856000
				elif(To=='Hectare'):
					y=x*0.4046856
				elif(To=='Acre'):
					y=x
				elif(To=='Square Mile(mi'+chr(178)+')'):
					y=x*0.00156249984
				elif(To=='Square Yard(yd'+chr(178)+')'):
					y=x*4839.99949
				elif(To=='Square Foot(ft'+chr(178)+')'):
					y=x*43559.9955
				else:
					y=x*6272639.35
			elif(From=='Square Mile(mi'+chr(178)+')'):
				if(To=='Square Km(Km'+chr(178)+')'):
					y=x*2.58998811
				elif(To=='Square Meter(m'+chr(178)+')'):
					y=x*2589988.11
				elif(To=='Square cm(cm'+chr(178)+')'):
					y=x*25899881100
				elif(To=='Square mm(mm'+chr(178)+')'):
					y=x*2589988110000
				elif(To=='Hectare'):
					y=x*258.998811
				elif(To=='Acre'):
					y=x*640.000067
				elif(To=='Square Mile(mi'+chr(178)+')'):
					y=x
				elif(To=='Square Yard(yd'+chr(178)+')'):
					y=x*3097600
				elif(To=='Square Foot(ft'+chr(178)+')'):
					y=x*27878400
				else:
					y=x*4014489600
			elif(From=='Square Yard(yd'+chr(178)+')'):
				if(To=='Square Km(Km'+chr(178)+')'):
					y=x*0.00000083612736
				elif(To=='Square Meter(m'+chr(178)+')'):
					y=x*0.83612736
				elif(To=='Square cm(cm'+chr(178)+')'):
					y=x*8361.2736
				elif(To=='Square mm(mm'+chr(178)+')'):
					y=x*836127.36
				elif(To=='Hectare'):
					y=x*0.000083612736
				elif(To=='Acre'):
					y=x*0.000206611592
				elif(To=='Square Mile(mi'+chr(178)+')'):
					y=x*0.000000322830579
				elif(To=='Square Yard(yd'+chr(178)+')'):
					y=x
				elif(To=='Square Foot(ft'+chr(178)+')'):
					y=x*9
				else:
					y=x*1296
			elif(From=='Square Foot(ft'+chr(178)+')'):
				if(To=='Square Km(Km'+chr(178)+')'):
					y=x*0.00000009290304
				elif(To=='Square Meter(m'+chr(178)+')'):
					y=x*0.09290304
				elif(To=='Square cm(cm'+chr(178)+')'):
					y=x*929.0304
				elif(To=='Square mm(mm'+chr(178)+')'):
					y=x*92903.04
				elif(To=='Hectare'):
					y=x*0.000009290304
				elif(To=='Acre'):
					y=x*0.0000229568435
				elif(To=='Square Mile(mi'+chr(178)+')'):
					y=x*0.0000000358700643
				elif(To=='Square Yard(yd'+chr(178)+')'):
					y=x*0.1111111111
				elif(To=='Square Foot(ft'+chr(178)+')'):
					y=x
				else:
					y=x*144
			else:
				if(To=='Square Km(Km'+chr(178)+')'):
					y=x*0.00000000064516
				elif(To=='Square Meter(m'+chr(178)+')'):
					y=x*0.00064516
				elif(To=='Square cm(cm'+chr(178)+')'):
					y=x*6.4516
				elif(To=='Square mm(mm'+chr(178)+')'):
					y=x*645.16
				elif(To=='Hectare'):
					y=x*0.000000064516
				elif(To=='Acre'):
					y=x*0.000000159422525
				elif(To=='Square Mile(mi'+chr(178)+')'):
					y=x*0.000000000249097669
				elif(To=='Square Yard(yd'+chr(178)+')'):
					y=x*0.000771604938
				elif(To=='Square Foot(ft'+chr(178)+')'):
					y=x*0.00694444445
				else:
					y=x
		elif(op=='vol'):
			if(From=='Cubic Meter(m'+chr(179)+')'):
				if(To=='Cubic Meter(m'+chr(179)+')'):
					y=x
				elif(To=='Cubic cm(cm'+chr(179)+')'):
					y=x*1000000
				elif(To=='Cubic mm(mm'+chr(179)+')'):
					y=x*1000000000
				elif(To=='Hectoliter'):
					y=x*10
				elif(To=='Liter'):
					y=x*1000
				elif(To=='Milliliter'):
					y=x*1000000
				elif(To=='Cubic Feet(ft'+chr(179)+')'):
					y=x*3146667
				else:
					y=x*61023.7441
			elif(From=='Cubic cm(cm'+chr(179)+')'):
				if(To=='Cubic Meter(m'+chr(179)+')'):
					y=x*0.000001
				elif(To=='Cubic cm(cm'+chr(179)+')'):
					y=x
				elif(To=='Cubic mm(mm'+chr(179)+')'):
					y=x*1000
				elif(To=='Hectoliter'):
					y=x*0.00001
				elif(To=='Liter'):
					y=x*0.001
				elif(To=='Milliliter'):
					y=x
				elif(To=='Cubic Feet(ft'+chr(179)+')'):
					y=x*0.0000353146668
				else:
					y=x*0.0610237441
			elif(From=='Cubic mm(mm'+chr(179)+')'):
				if(To=='Cubic Meter(m'+chr(179)+')'):
					y=x*0.000000001
				elif(To=='Cubic cm(cm'+chr(179)+')'):
					y=x*0.001
				elif(To=='Cubic mm(mm'+chr(179)+')'):
					y=x
				elif(To=='Hectoliter'):
					y=x*0.00000001
				elif(To=='Liter'):
					y=x*0.000001
				elif(To=='Milliliter'):
					y=x*0.001
				elif(To=='Cubic Feet(ft'+chr(179)+')'):
					y=x*0.0000000353146668
				else:
					y=x*0.0000610237441
			elif(From=='Hectoliter'):
				if(To=='Cubic Meter(m'+chr(179)+')'):
					y=x*0.1
				elif(To=='Cubic cm(cm'+chr(179)+')'):
					y=x*100000
				elif(To=='Cubic mm(mm'+chr(179)+')'):
					y=x*100000000
				elif(To=='Hectoliter'):
					y=x
				elif(To=='Liter'):
					y=x*100
				elif(To=='Milliliter'):
					y=x*100000
				elif(To=='Cubic Feet(ft'+chr(179)+')'):
					y=x*3.53146668
				else:
					y=x*6102.37441
			elif(From=='Liter'):
				if(To=='Cubic Meter(m'+chr(179)+')'):
					y=x*0.001
				elif(To=='Cubic cm(cm'+chr(179)+')'):
					y=x*1000
				elif(To=='Cubic mm(mm'+chr(179)+')'):
					y=x*1000000
				elif(To=='Hectoliter'):
					y=x*0.01
				elif(To=='Liter'):
					y=x
				elif(To=='Milliliter'):
					y=x*1000
				elif(To=='Cubic Feet(ft'+chr(179)+')'):
					y=x*0.0353146668
				else:
					y=x*61.0237441
			elif(From=='Milliliter'):
				if(To=='Cubic Meter(m'+chr(179)+')'):
					y=x*0.000001
				elif(To=='Cubic cm(cm'+chr(179)+')'):
					y=x
				elif(To=='Cubic mm(mm'+chr(179)+')'):
					y=x*1000
				elif(To=='Hectoliter'):
					y=x*0.00001
				elif(To=='Liter'):
					y=x*0.001
				elif(To=='Milliliter'):
					y=x
				elif(To=='Cubic Feet(ft'+chr(179)+')'):
					y=x*0.0000353146668
				else:
					y=x*0.0610237441
			elif(From=='Cubic Feet(ft'+chr(179)+')'):
				if(To=='Cubic Meter(m'+chr(179)+')'):
					y=x*0.0283168466
				elif(To=='Cubic cm(cm'+chr(179)+')'):
					y=x*28316.8466
				elif(To=='Cubic mm(mm'+chr(179)+')'):
					y=x*28316846.6
				elif(To=='Hectoliter'):
					y=x*0.283168466
				elif(To=='Liter'):
					y=x*28.3168466
				elif(To=='Milliliter'):
					y=x*28316.8466
				elif(To=='Cubic Feet(ft'+chr(179)+')'):
					y=x
				else:
					y=x*1728
			else:
				if(To=='Cubic Meter(m'+chr(179)+')'):
					y=x*0.000016387064
				elif(To=='Cubic cm(cm'+chr(179)+')'):
					y=x*16.387064
				elif(To=='Cubic mm(mm'+chr(179)+')'):
					y=x*16387.064
				elif(To=='Hectoliter'):
					y=x*0.00016387064
				elif(To=='Liter'):
					y=x*0.016387064
				elif(To=='Milliliter'):
					y=x*16.387064
				elif(To=='Cubic Feet(ft'+chr(179)+')'):
					y=x*0.000578703704
				else:
					y=x
		elif(op=='mass'):
			if(From=='Tonne(t)'):
				if(To=='Tonne(t)'):
					y=x
				elif(To=='Kilogram(Kg)'):
					y=x*1000
				elif(To=='Gram(g)'):
					y=x*1000000
				elif(To=='Milligram(mg)'):
					y=x*1000000000
				elif(To=='Quintal(q)'):
					y=x*10
				elif(To=='Pound(lb)'):
					y=x*2204.62262
				else:
					y=x*35273.9619
			elif(From=='Kilogram(Kg)'):
				if(To=='Tonne(t)'):
					y=x*0.001
				elif(To=='Kilogram(Kg)'):
					y=x
				elif(To=='Gram(g)'):
					y=x*1000
				elif(To=='Milligram(mg)'):
					y=x*1000000
				elif(To=='Quintal(q)'):
					y=x*0.01
				elif(To=='Pound(lb)'):
					y=x*2.20462262
				else:
					y=x*35.2739619
			elif(From=='Gram(g)'):
				if(To=='Tonne(t)'):
					y=x*0.000001
				elif(To=='Kilogram(Kg)'):
					y=x*0.001
				elif(To=='Gram(g)'):
					y=x
				elif(To=='Milligram(mg)'):
					y=x*1000
				elif(To=='Quintal(q)'):
					y=x*0.00001
				elif(To=='Pound(lb)'):
					y=x*0.00220462262
				else:
					y=x*0.0352739619
			elif(From=='Milligram(mg)'):
				if(To=='Tonne(t)'):
					y=x*0.000000001
				elif(To=='Kilogram(Kg)'):
					y=x*0.000001
				elif(To=='Gram(g)'):
					y=x*0.001
				elif(To=='Milligram(mg)'):
					y=x
				elif(To=='Quintal(q)'):
					y=x*0.00000001
				elif(To=='Pound(lb)'):
					y=x*0.00000220462262
				else:
					y=x*0.0000352739619
			elif(From=='Quintal(q)'):
				if(To=='Tonne(t)'):
					y=x*0.1
				elif(To=='Kilogram(Kg)'):
					y=x*100
				elif(To=='Gram(g)'):
					y=x*100000
				elif(To=='Milligram(mg)'):
					y=x*100000000
				elif(To=='Quintal(q)'):
					y=x
				elif(To=='Pound(lb)'):
					y=x*220.462262
				else:
					y=x*3527.39619
			elif(From=='Pound(lb)'):
				if(To=='Tonne(t)'):
					y=x*0.0004535937
				elif(To=='Kilogram(Kg)'):
					y=x*0.4535937
				elif(To=='Gram(g)'):
					y=x*453.59237
				elif(To=='Milligram(mg)'):
					y=x*453592.37
				elif(To=='Quintal(q)'):
					y=x*0.0045359237
				elif(To=='Pound(lb)'):
					y=x
				else:
					y=x*16
			else:
				if(To=='Tonne(t)'):
					y=x*0.0000283495231
				elif(To=='Kilogram(Kg)'):
					y=x*0.0283495231
				elif(To=='Gram(g)'):
					y=x*28.3495231
				elif(To=='Milligram(mg)'):
					y=x*28349.5231
				elif(To=='Quintal(q)'):
					y=x*0.000283495231
				elif(To=='Pound(lb)'):
					y=x*0.0625
				else:
					y=x
		elif(op=='temp'):
			if(From=='Celsius('+chr(176)+'C)'):
				if(To=='Celsius('+chr(176)+'C)'):
					y=x
				elif(To=='Farenheit('+chr(176)+'F)'):
					y=(x*1.8)+32
				else:
					y=x+273.15
			if(From=='Farenheit('+chr(176)+'F)'):
				if(To=='Celsius('+chr(176)+'C)'):
					y=(x-32)*0.555556
				elif(To=='Farenheit('+chr(176)+'F)'):
					y=x
				else:
					y=((x-32)*0.555556)+273.15
			else:
				if(To=='Celsius('+chr(176)+'C)'):
					y=x-273.15
				elif(To=='Farenheit('+chr(176)+'F)'):
					y=((x-273.15)*1.8)+32
				else:
					y=x
		elif(op=='speed'):
			if(From=='Light Speed(C)'):
				if(To=='Light Speed(C)'):
					y=x
				elif(To=='Mach(Ma)'):
					y=x*880965.201
				elif(To=='Meter/Speed(mps)'):
					y=x*299792458
				elif(To=='Kilometer/Hour(Kmph)'):
					y=x*1079252850
				elif(To=='Knot(kn)'):
					y=x*582749918
				else:
					y=x*670616629
			elif(From=='Mach(Ma)'):
				if(To=='Light Speed(C)'):
					y=x*0.00000113511862
				elif(To=='Mach(Ma)'):
					y=x
				elif(To=='Meter/Speed(mps)'):
					y=x*340.3
				elif(To=='Kilometer/Hour(Kmph)'):
					y=x*1225.08
				elif(To=='Knot(kn)'):
					y=x*661.490281
				else:
					y=x*761.22942
			elif(From=='Meter/Speed(mps)'):
				if(To=='Light Speed(C)'):
					y=x*0.0000000033564095
				elif(To=='Mach(Ma)'):
					y=x*0.0029385836
				elif(To=='Meter/Speed(mps)'):
					y=x
				elif(To=='Kilometer/Hour(Kmph)'):
					y=x*3.6
				elif(To=='Knot(kn)'):
					y=x*1.94384449
				else:
					y=x*2.3693629
			elif(From=='Kilometer/Hour(Kmph)'):
				if(To=='Light Speed(C)'):
					y=x*0.000000000926566931
				elif(To=='Mach(Ma)'):
					y=x*0.000816273223
				elif(To=='Meter/Speed(mps)'):
					y=x*0.27777777777778
				elif(To=='Kilometer/Hour(Kmph)'):
					y=x
				elif(To=='Knot(kn)'):
					y=x*0.539956803
				else:
					y=x*0.621371192
			elif(From=='Knot(kn)'):
				if(To=='Light Speed(C)'):
					y=x*0.00000000171600196
				elif(To=='Mach(Ma)'):
					y=x*0.00151173801
				elif(To=='Meter/Speed(mps)'):
					y=x*0.5144444444444
				elif(To=='Kilometer/Hour(Kmph)'):
					y=x*1.852
				elif(To=='Knot(kn)'):
					y=x
				else:
					y=x*1.15077945
			else:
				if(To=='Light Speed(C)'):
					y=x*0.000000001491164934
				elif(To=='Mach(Ma)'):
					y=x*0.0013136641
				elif(To=='Meter/Speed(mps)'):
					y=x*0.44704
				elif(To=='Kilometer/Hour(Kmph)'):
					y=x*1.609344
				elif(To=='Knot(kn)'):
					y=x*0.868976242
				else:
					y=x
		else:
			if(From=='Seconds'):
				if(To=='Seconds'):
					y=x
				elif(To=='Minutes'):
					y=x*0.016666666666667
				elif(To=='Hour'):
					y=x*0.000277777777778
				elif(To=='Days'):
					y=x*0.0000115740741
				elif(To=='Weeks'):
					y=x*0.00000165343915
				else:
					y=x*0.000000031709792
			elif(From=='Minutes'):
				if(To=='Seconds'):
					y=x*60
				elif(To=='Minutes'):
					y=x
				elif(To=='Hour'):
					y=x*0.0166666666666667
				elif(To=='Days'):
					y=x*0.0006944444444444
				elif(To=='Weeks'):
					y=x*0.0000992063492
				else:
					y=x*0.00000190258752
			elif(From=='Hour'):
				if(To=='Seconds'):
					y=x*3600
				elif(To=='Minutes'):
					y=x*60
				elif(To=='Hour'):
					y=x
				elif(To=='Days'):
					y=x*0.04166666666667
				elif(To=='Weeks'):
					y=x*0.00595238095
				else:
					y=x*0.000114155251
			elif(From=='Days'):
				if(To=='Seconds'):
					y=x*86400
				elif(To=='Minutes'):
					y=x*1440
				elif(To=='Hour'):
					y=x*24
				elif(To=='Days'):
					y=x
				elif(To=='Weeks'):
					y=x*0.142857143
				else:
					y=x*0.00273972603
			elif(From=='Weeks'):
				if(To=='Seconds'):
					y=x*604800
				elif(To=='Minutes'):
					y=x*10080
				elif(To=='Hour'):
					y=x*168
				elif(To=='Days'):
					y=x*7
				elif(To=='Weeks'):
					y=x
				else:
					y=x*0.0191780822
			else:
				if(To=='Seconds'):
					y=x*31536000
				elif(To=='Minutes'):
					y=x*525600
				elif(To=='Hour'):
					y=x*8760
				elif(To=='Days'):
					y=x*365
				elif(To=='Weeks'):
					y=x*52.142857
				else:
					y=x
		txtTo.insert(END,str(y))

fileMenu=Menu(menubar)
fileMenu.config(bg='#666666',activebackground='#333333',activeforeground='#ffffff')
menubar.add_cascade(label='File',menu=fileMenu)
fileMenu.add_separator()
fileMenu.add_command(label='Home',command=fnHome)
fileMenu.add_command(label='Exit',command=window.quit)

fnHome()

window.mainloop()
