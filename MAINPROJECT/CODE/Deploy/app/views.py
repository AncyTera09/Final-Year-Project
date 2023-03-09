from django.shortcuts import render
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from tensorflow import keras

from . import forms
from .models import UserImageModel

# Create your views here.
def home(request):
    print("HI")
    if request.method == "POST":
        form = forms.UserImageForm(files=request.FILES)
        if form.is_valid():
            print('HIFORM')
            form.save()
        obj = form.instance
        #('obj',obj)
        result = UserImageModel.objects.latest('id')
        result = result.image           
        models = keras.models.load_model('C:/Users/Hp/Downloads/CODE/CODE/Deploy/app/LeNet.h5')
        from tensorflow.keras.preprocessing import image
        test_image = image.load_img('C:/Users/Hp/Downloads/CODE/CODE/Deploy/media/' + str(result),
                                    target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = models.predict(test_image)
        prediction = result[0]
        prediction = list(prediction)
        classes = ['Clothes_Fabrics','Electrical_Instuments','Glass_Bottles','Metals_Instruments','Pills_Tablets','Plastics_Polymers','Tonics_Liquid_Chemicals']
        output = zip(classes, prediction)
        output = dict(output)
        if output['Clothes_Fabrics'] == 1.0:
            a='Clothes_Fabrics'
            b='NON TOXIC'
            c= 'Medical fabrics are typically made from high-quality materials that can withstand repeated washing and sterilization. The fabrics are typically sent to a specialized recycling facility where they are cleaned, sanitized, and processed using industrial textile recycling equipment. Once the fabrics have been processed, they can be recycled into a variety of end products, such as new medical fabrics, insulation, or even carpet padding.'
            d= 'Sterilization techniques involved: Autoclaving, Gamma irradiation, Ethylene Oxide Sterilization, Hydrogen peroxide gas sterilization, UV irradiation'
            e='ReNewcell Texpertise Pvt Ltd: Website://amkayproducts.com/contact-us/'
        elif output['Electrical_Instuments'] == 1.0:
            a='Electrical_Instuments'
            b='NON TOXIC'
            c='Recycling of medical electric instruments involves the recovery of valuable metals and other materials from the instruments, which can then be reused in other applications.  Alternatively, medical electric instruments may be treated as electronic waste and processed in specialized facilities that are equipped to handle these types of materials.'
            d= 'Sterilization techniques involved : Recycling techniques: Reprocessing, Refurbishment, Donation etc.'
            e= 'Kirti Healthcare Pvt Ltd:Website: /www.kirtii.com/, PK Traders:Website:www.tradeindia.com/pk-traders-26238488/product-services.html'
        elif output['Glass_Bottles'] == 1.0:
            a="Glass_Bottles"
            b='NON TOXIC'
            c='Usually, medical glasses are highly contagious hence they undergo a series of sterilization processes.  The sterilized glass is crushed into small pieces called “cullet”  and then melted in a furnace at about 1500 degree celsius.  The crushed glass can also be added to road construction materials.  The melted glass after removing impurities can be reshaped into desired products. '
            d='Sterilization techniques involved : Autoclaving, Chemical Sterilization, Radiation Sterilization.'
            e='Aries Technical Services Pvt Ltd:Website:aeriestechnology.com, Virogreen India Pvt. Ltd :  Website:www.virogreen.in/'       
        elif output['Metals_Instruments'] == 1.0:
            a="Metals_Instruments"
            b='NON TOXIC'
            c='Medical metal wastes such as syringe needles, surgical sharps including scissors, forceps, etc. are usually recycled through a process known as metal reclamation or metal recycling. This process involves collecting the metal waste, segregating them based on their type and grade, and then they are shredded, smelted, refined and formed into desired product.'
            d='Sterilization techniques involved : Autoclaving, Chemical Disinfection, Microwave Sterilization.'
            e='Virogreen India Pvt. Ltd.:  Website:www.virogreen.in/, E-waste Recyclers India:Website: www.earthsenserecycle.com/'
        elif output['Pills_Tablets'] == 1.0:
            a="Pills_Tablets"
            b='TOXIC'
            c='Discarded pills can either be repurposed for use in clinical trials or they can be made to undergo a process of controlled incineration where pills are burned at high temperature until they turn into ash.  The controlled incineration process is involved because it does not release the harmful pollutants into air as pills are chemicals and certain chemicals pose as risk when not incinerated controllably.  Incineration ash can be used for productive purposes such as in construction materials like bricks, cement and concrete or  road construction materials like asphalt, or as a soil amendment.'
            d='Sterilization techniques involved :  Controlled Incineration'
            e='Ramky Enviro Engineers Ltd :Website: ramkyenviroengineers.com/, A2Z Groups:Website:www.a2zgroup.co.in/'
        elif output['Plastics_Polymers'] == 1.0:
            a="Plastics_Polymers"
            b='NON TOXIC'
            c='Medical plastics, such as syringes, IV bags, and tubing, can be recycled through several methods. The specific method used depends on the type of plastic and the level of contamination.  It includes various techniques such as, Mechanical recycling: This involves grinding the medical plastic waste into small flakes or pellets, which can then be melted and used to make new products.  Chemical recycling: This method breaks down the plastic waste into its chemical components, which can then be used to make new plastic products.  Pyrolysis: This involves heating the medical plastic waste to high temperatures in the absence of oxygen, which breaks down the plastic into its chemical components. These components can then be used to make new products or fuels.  Energy recovery: This involves burning the medical plastic waste to generate energy, such as steam or electricity.'
            d='Sterilization techniques involved : Autoclaving, Gamma irradiation, Ethylene Oxide Sterilization, UV-C Sterilization.'
            e='GEM Enviro Management Pvt Ltd: gemrecycling.com, Vinsak India PVT LTD:https://vinsak.com/about-us/'
        elif output['Tonics_Liquid_Chemicals'] == 1.0:
            a="Tonics_Liquid_Chemicals"
            b='TOXIC'
            c='Autoclaving, Gamma irradiation, Ethylene Oxide Sterilization, UV-C Sterilization.'
            d='Autoclaving, Gamma irradiation, Ethylene Oxide Sterilization, UV-C Sterilization.'
            e='Autoclaving, Gamma irradiation, Ethylene Oxide Sterilization, UV-C Sterilization.'
             
        
        return render(request, 'app/index.html',{'form':form,'obj':obj,'predict1':b,'predict2':a,'predict3':c,'predict4':d,'predict5':e})
    else:
        form = forms.UserImageForm()
    return render(request, 'app/index.html',{'form':form})

