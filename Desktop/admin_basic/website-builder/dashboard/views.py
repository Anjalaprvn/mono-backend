from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def login_view(request):
	"""Render the login page and handle login."""
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		remember = request.POST.get('remember')
		
		# For now, simple authentication - in production, use proper user authentication
		# This is a placeholder - you should implement actual user authentication
		if email and password:
			# Check if credentials are valid (replace with actual authentication)
			# user = authenticate(request, username=email, password=password)
			# if user is not None:
			#     login(request, user)
			#     if remember:
			#         request.session.set_expiry(1209600)  # 2 weeks
			#     return redirect('dashboard:index')
			# else:
			#     return redirect('dashboard:login?message=Invalid email or password. Please try again.&type=error')
			
			# Temporary: For demo purposes, accept any email/password
			# In production, replace this with proper authentication
			return redirect('dashboard:index')
		else:
			return redirect('dashboard:login?message=Please enter both email and password.&type=error')
	
	# Get messages from Django messages framework if any
	context = {}
	return render(request, "login.html", context)


def logout_view(request):
	"""Handle user logout."""
	logout(request)
	# Redirect with logout message
	return redirect('dashboard:login?message=You have been successfully logged out.&type=success')


def index(request):
	"""Render the dashboard index page."""
	context = {
		'page_title': 'Dashboard',
		'page_subtitle': 'Welcome back to Vastu Farms Admin Portal',
		'current_page': 'dashboard',
	}
	return render(request, "index.html", context)


def plots_list(request):
	"""Render the plots listing page."""
	# Sample property data
	properties = [
		{
			'id': 1,
			'name': 'Golden Fields - Plot F8',
			'image': '/static/img/property1.jpg',
			'price': '41.5L',
			'vastu_score': 72,
			'area': '3,000',
			'facing': 'South-East',
			'status': 'Sold',
			'featured': True,
		},
		{
			'id': 2,
			'name': 'Sunrise Valley - Plot A3',
			'image': '/static/img/property2.jpg',
			'price': '38.2L',
			'vastu_score': 85,
			'area': '2,500',
			'facing': 'East',
			'status': 'Available',
			'featured': False,
		},
		{
			'id': 3,
			'name': 'Green Meadows - Plot C5',
			'image': '/static/img/property3.jpg',
			'price': '52.0L',
			'vastu_score': 68,
			'area': '4,200',
			'facing': 'North',
			'status': 'Reserved',
			'featured': True,
		},
		{
			'id': 4,
			'name': 'Lakeside Estate - Plot D2',
			'image': '/static/img/property4.jpg',
			'price': '65.8L',
			'vastu_score': 91,
			'area': '5,000',
			'facing': 'North-East',
			'status': 'Available',
			'featured': False,
		},
		{
			'id': 5,
			'name': 'Hilltop Gardens - Plot B7',
			'image': '/static/img/property5.jpg',
			'price': '45.0L',
			'vastu_score': 78,
			'area': '3,500',
			'facing': 'West',
			'status': None,
			'featured': False,
		},
		{
			'id': 6,
			'name': 'River View - Plot E1',
			'image': '/static/img/property6.jpg',
			'price': '58.5L',
			'vastu_score': 82,
			'area': '4,000',
			'facing': 'South',
			'status': 'Available',
			'featured': True,
		},
	]

	context = {
		'properties': properties,
		'page_title': 'Property Management',
		'page_subtitle': 'Manage all your farm plots and land listings',
		'current_page': 'plots',
	}
	return render(request, "plots/list.html", context)

def plot_add(request):
	"""Render the plot add page."""
	context = {
		'page_title': 'Register New Plot',
		'page_subtitle': 'Add a new land listing to Vastu Farms',
		'current_page': 'Add plots',
	}
	return render(request, "plots/add.html", context)

def plot_edit(request, pk):
	"""Render the plot edit page."""
	# Sample plot data - in production, fetch from database using pk
	plot = {
		'id': pk,
		'name': 'Golden Fields - Plot F8',
		'location': 'Bangalore Rural, Karnataka',
		'size': '3,000',
		'price': '41.5',
		'description': 'A beautiful plot with excellent Vastu compliance and scenic views.',
		'facing': 'SE',
		'nakshatras': ['Ashwini', 'Rohini', 'Pushya'],
		'reasons': [
			'Excellent alignment with cardinal directions',
			'Natural water flow towards North-East',
		],
		'highlights': [
			'Corner plot with road on two sides',
			'Mature trees on boundary',
			'Underground water available',
		],
		'nearby_places': [
			{'destination': 'Bangalore City Center', 'distance': '45km'},
			{'destination': 'International Airport', 'distance': '35km'},
		],
		'media': [
			{'id': '1', 'url': '/static/img/property1.jpg', 'name': 'property1.jpg'},
			{'id': '2', 'url': '/static/img/property2.jpg', 'name': 'property2.jpg'},
		],
	}
	
	# Nakshatra options for the form
	nakshatra_options = [
		'Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra',
		'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'Purva Phalguni', 
		'Uttara Phalguni', 'Hasta', 'Chitra', 'Swati', 'Vishakha', 
		'Anuradha', 'Jyeshtha', 'Mula', 'Purva Ashadha', 'Uttara Ashadha',
		'Shravana', 'Dhanishta', 'Shatabhisha', 'Purva Bhadrapada', 
		'Uttara Bhadrapada', 'Revati'
	]
	
	import json
	context = {
		'plot': plot,
		'plot_nakshatras_json': json.dumps(plot['nakshatras']),
		'plot_media_count': len(plot['media']),
		'nakshatra_options': nakshatra_options,
		'page_title': 'Edit Plot',
		'page_subtitle': 'Edit the existing plot details',
		'current_page': 'plots',
	}
	return render(request, "plots/edit.html", context)

def plot_view(request, pk):
	"""Render the plot view page."""
	# Sample plot data - in production, fetch from database using pk
	plot = {
		'id': pk,
		'name': 'Golden Fields - Plot F8',
		'location': 'Sunrise Meadows, Block A',
		'size': '2,400',
		'price': '32.4L',
		'description': 'Beautiful east-facing plot with scenic views',
		'facing': 'E',
		'vastu_score': 92,
		'status': 'Available',
		'is_sold': False,
		'created_date': '15 January 2024',
		'image': '/static/dashboard/img/vastu-logo.png',
		'nakshatras': [
			{
				'name': 'Ashwini',
				'reason': 'East-facing plots are auspicious for Ashwini natives as it aligns with their dynamic energy.'
			},
			{
				'name': 'Rohini',
				'reason': 'The fertile land and morning sun exposure suits Rohini creativity.'
			},
		],
		'highlights': [
			'Corner plot with road on two sides',
			'Mature trees on boundary',
			'Underground water available',
		],
		'nearby_places': [
			{'destination': 'Temple', 'distance': '2km'},
			{'destination': 'School', 'distance': '3km'},
			{'destination': 'Hospital', 'distance': '5km'},
		],
		'media': [],  # Empty to show "No media files uploaded"
	}
	context = {
		'plot': plot,
		'page_title': 'View Plot',
		'page_subtitle': 'View details of a specific plot',
		'current_page': 'plots',
	}
	return render(request, "plots/view.html", context)


def enquiry_list(request):
	"""Render the enquiry listing page."""
	# Sample enquiry data
	enquiries = [
		{
			'id': 1,
			'full_name': 'Rajesh Kumar',
			'email': 'rajesh.kumar@email.com',
			'phone': '+91 98765 43210',
			'subject': 'Plot Inquiry',
			'message': 'I am interested in the Golden Fields plot. Please share more details about the pricing and availability.',
			'status': 'Not Attended',
		},
		{
			'id': 2,
			'full_name': 'Priya Sharma',
			'email': 'priya.sharma@email.com',
			'phone': '+91 87654 32109',
			'subject': 'Site Visit Request',
			'message': 'Would like to schedule a site visit for Sunrise Valley plots this weekend.',
			'status': 'Attended',
		},
		{
			'id': 3,
			'full_name': 'Amit Patel',
			'email': 'amit.patel@email.com',
			'phone': '+91 76543 21098',
			'subject': 'Vastu Consultation',
			'message': 'Need information about Vastu compliance for the east-facing plots.',
			'status': 'Not Attended',
		},
		{
			'id': 4,
			'full_name': 'Sunita Verma',
			'email': 'sunita.verma@email.com',
			'phone': '+91 65432 10987',
			'subject': 'Payment Options',
			'message': 'What are the EMI options available for plot purchase?',
			'status': 'Attended',
		},
		{
			'id': 5,
			'full_name': 'Vikram Singh',
			'email': 'vikram.singh@email.com',
			'phone': '+91 54321 09876',
			'subject': 'Documentation Query',
			'message': 'Please provide the list of documents required for plot registration.',
			'status': 'Not Attended',
		},
	]

	context = {
		'enquiries': enquiries,
		'page_title': 'Enquiries',
		'page_subtitle': 'Manage customer enquiries and requests',
		'current_page': 'enquiry',
	}
	return render(request, "enquiry.html", context)


def blog_list(request):
	"""Render the blog posts listing page."""
	# Sample blog data
	posts = [
		{
			'id': 1,
			'title': 'Understanding Vastu for Agricultural Land',
			'excerpt': 'Learn how ancient Vastu principles can enhance the prosperity of your agricultural investments.',
			'author': 'Dr. Ramesh Sharma',
			'category': 'Vastu Tips',
			'status': 'Published',
			'date': '2024-01-15',
			'views': '1,245',
		},
		{
			'id': 2,
			'title': 'Best Nakshatras for Land Purchase',
			'excerpt': 'Discover which lunar mansions are most auspicious for buying agricultural land.',
			'author': 'Dr. Ramesh Sharma',
			'category': 'Astrology',
			'status': 'Published',
			'date': '2024-01-15',
			'views': '892',
		},
		{
			'id': 3,
			'title': 'Why East-Facing Plots Command Premium Prices',
			'excerpt': 'The science behind directional preferences in Vastu and their impact on property values.',
			'author': 'Dr. Ramesh Sharma',
			'category': 'Investment',
			'status': 'Draft',
			'date': '2024-01-15',
			'views': '0',
		},
		{
			'id': 4,
			'title': 'Organic Farming: A Vastu-Aligned Approach',
			'excerpt': 'Combine traditional wisdom with modern organic farming practices for better yields.',
			'author': 'Dr. Ramesh Sharma',
			'category': 'Farming',
			'status': 'Published',
			'date': '2024-01-15',
			'views': '0',
		},
	]

	context = {
		'posts': posts,
		'page_title': 'Blog Posts',
		'page_subtitle': 'Create and manage blog content for your website',
		'current_page': 'blog',
	}
	return render(request, "blogs/list.html", context)


def blog_add(request):
	"""Render the add blog post page."""
	context = {
		'page_title': 'Create New Post',
		'page_subtitle': 'Add a new blog post to your website',
		'current_page': 'blog',
	}
	return render(request, "blogs/add.html", context)


def blog_view(request):
	"""Render the blog detail page."""
	# Sample blog data - in production, fetch from database using pk
	blog = {
		'id': 1,
		'title': 'Why East-Facing Plots Command Premium Prices',
		'author': 'Dr. Ramesh Sharma',
		'image': '/static/img/vastu-logo.png',
		'date': '26/12/2025',
		'time': '11:30 AM',
		'description': 'The universe is composed of five great elements: Prithvi (Earth), Jal (Water), Agni (Fire), Vayu (Air), and Aakash (Space). Vastu Shastra is the science of balancing these elements within a bounded space. Balancing the Elements When selecting a plot, we look for natural indicators of these elements. A slope towards the North-East suggests a positive flow of the Water element, while a heavier, elevated South-West strengthens the Earth element.',
	}
	context = {
		'blog': blog,
		'page_title': 'Blog Posts',
		'page_subtitle': 'Create and manage blog content for your website',
		'current_page': 'blog',
	}
	return render(request, "blogs/view.html", context)


def payment_history(request):
	"""Render the payment history page."""
	context = {
		'page_title': 'Payment History',
		'page_subtitle': 'View all payment transactions',
		'current_page': 'payment',
	}
	return render(request, "payment.html", context)


def token_management(request):
	"""Render the token management page."""
	context = {
		'page_title': 'Token Management',
		'page_subtitle': 'Manage plot tokens and bookings',
		'current_page': 'token',
	}
	return render(request, "token.html", context)


def lead_management(request):
	"""Render the lead management page."""
	context = {
		'page_title': 'Lead Management',
		'page_subtitle': 'Track and manage potential buyer inquiries',
		'current_page': 'leads',
	}
	return render(request, "lead.html", context)


def matching_engine(request):
	"""Render the Nakshatra Matching Engine page."""
	nakshatras = [
		{'id': 1, 'name': 'Ashwini', 'ruler': 'Ashwini Kumaras', 'symbol': '🐴', 'directions': 'S,SE,SW', 'shapes': 'square'},
		{'id': 2, 'name': 'Bharani', 'ruler': 'Yama', 'symbol': '🔴', 'directions': 'E,SE', 'shapes': 'rectangle'},
		{'id': 3, 'name': 'Krittika', 'ruler': 'Agni', 'symbol': '🔥', 'directions': 'N,NE', 'shapes': 'triangle'},
		{'id': 4, 'name': 'Rohini', 'ruler': 'Brahma', 'symbol': '🐂', 'directions': 'E,NE', 'shapes': 'square,rectangle'},
		{'id': 5, 'name': 'Mrigashira', 'ruler': 'Soma', 'symbol': '🦌', 'directions': 'N,NW', 'shapes': 'rectangle'},
		{'id': 6, 'name': 'Ardra', 'ruler': 'Rudra', 'symbol': '💧', 'directions': 'W,NW', 'shapes': 'irregular'},
		{'id': 7, 'name': 'Punarvasu', 'ruler': 'Aditi', 'symbol': '🏹', 'directions': 'N,NE,E', 'shapes': 'square'},
		{'id': 8, 'name': 'Pushya', 'ruler': 'Brihaspati', 'symbol': '🌸', 'directions': 'N,E', 'shapes': 'square,rectangle'},
		{'id': 9, 'name': 'Ashlesha', 'ruler': 'Nagas', 'symbol': '💚', 'directions': 'S,SW', 'shapes': 'irregular'},
		{'id': 10, 'name': 'Magha', 'ruler': 'Pitrs', 'symbol': '👑', 'directions': 'S,SE', 'shapes': 'square'},
		{'id': 11, 'name': 'Purva Phalguni', 'ruler': 'Bhaga', 'symbol': '🛏️', 'directions': 'E,SE', 'shapes': 'rectangle'},
		{'id': 12, 'name': 'Uttara Phalguni', 'ruler': 'Aryaman', 'symbol': '🌞', 'directions': 'E,NE', 'shapes': 'square'},
		{'id': 13, 'name': 'Hasta', 'ruler': 'Savitar', 'symbol': '✋', 'directions': 'N,NE', 'shapes': 'pentagon'},
		{'id': 14, 'name': 'Chitra', 'ruler': 'Vishwakarma', 'symbol': '💎', 'directions': 'S,SW', 'shapes': 'hexagon'},
		{'id': 15, 'name': 'Swati', 'ruler': 'Vayu', 'symbol': '🌿', 'directions': 'W,NW', 'shapes': 'rectangle'},
		{'id': 16, 'name': 'Vishakha', 'ruler': 'Indra-Agni', 'symbol': '🌳', 'directions': 'E,SE', 'shapes': 'triangle'},
		{'id': 17, 'name': 'Anuradha', 'ruler': 'Mitra', 'symbol': '🌺', 'directions': 'N,S', 'shapes': 'square'},
		{'id': 18, 'name': 'Jyeshtha', 'ruler': 'Indra', 'symbol': '👂', 'directions': 'S,SW', 'shapes': 'pentagon'},
		{'id': 19, 'name': 'Mula', 'ruler': 'Nirriti', 'symbol': '🦁', 'directions': 'S,SE', 'shapes': 'irregular'},
		{'id': 20, 'name': 'Purva Ashadha', 'ruler': 'Apas', 'symbol': '🌊', 'directions': 'E,SE', 'shapes': 'rectangle'},
		{'id': 21, 'name': 'Uttara Ashadha', 'ruler': 'Vishvadevas', 'symbol': '🐘', 'directions': 'N,NE', 'shapes': 'square'},
		{'id': 22, 'name': 'Shravana', 'ruler': 'Vishnu', 'symbol': '👂', 'directions': 'N,NW', 'shapes': 'square,rectangle'},
		{'id': 23, 'name': 'Dhanishta', 'ruler': 'Vasus', 'symbol': '🥁', 'directions': 'E,W', 'shapes': 'hexagon'},
		{'id': 24, 'name': 'Shatabhisha', 'ruler': 'Varuna', 'symbol': '⭐', 'directions': 'S,SW', 'shapes': 'irregular'},
		{'id': 25, 'name': 'Purva Bhadrapada', 'ruler': 'Aja Ekapada', 'symbol': '⚔️', 'directions': 'W,NW', 'shapes': 'rectangle'},
		{'id': 26, 'name': 'Uttara Bhadrapada', 'ruler': 'Ahir Budhnya', 'symbol': '🐍', 'directions': 'N,NE', 'shapes': 'square'},
		{'id': 27, 'name': 'Revati', 'ruler': 'Pushan', 'symbol': '🐟', 'directions': 'E,NE', 'shapes': 'pentagon'},
	]
	context = {
		'page_title': 'Nakshatra Matching Engine',
		'page_subtitle': 'Configure the 27 lunar mansions and their Vastu compatibility rules',
		'current_page': 'matching',
		'nakshatras': nakshatras,
	}
	return render(request, "matchengine.html", context)
