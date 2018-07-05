
This project mainly provides search application solution for web application using Apache solr search platform which uses REST based url to query the data for faster accessing of data using two approaches to implement the approaches are: 

1) Using Django Framework
2) Using javascript,HTML and CSS approach.

Preference of implementation
 1) Django framework
      If you are using django framework for your application and if you want query should be sent from python code(from     server) to apache solr you can use the first approach but doesn't have paginated result and auto suggestion feature but auto suggestion can be implemented by using django select2 widget details documentation are in following link
        http://django-select2.readthedocs.io/en/latest/
   
2) Javascript HTML and CSS approach.
      These can be run at client side and doesn't require any server to run and querie is done from ajax code. This approach also has feature of auto suggestion and paginated result. if you want to run query the apache solr irrespective of frameworks then second approach can be used.

Pre requities to run the code:
1) Apache solr Search platform 
2) Django framework (to django Framework approach
3) You need to have cors plugin in chrome at development stage (to avoid CROS error while using second approach)



Pre requities Installation Steps 

1. Apache solr and running into local machine.
	
	1.1  Download latest version of apache solr from the following link(zip file)
			http://archive.apache.org/dist/lucene/solr/
	
	1.2  And Extract the zip file

	1.3  Open terminal and goto the downloaded folder path 
		
		now your terminal path will be 
			$<directory path>/solr-X.X.

	
	1.4  Running the apache solr
		Once you are in solr folder type the fillowing command to   Start the apache solr server 
			
			$ bin/solr start	

2. Django framework installation
    Django 2 runs on Python3. 
    2.1 Install python3 from the following comman
             $sudo apt-get update
            $sudo apt-get install python3.6 
 
    2.2  Setting up virtual Environment for development
         Execute the following commands to set up virtual environment
         $ sudo pip install virtualenv

            Usage 		
            Virtualenv has basic command
                    $virtualenv ENV

            Where env is directory to place the new virtual environment.
            
            To activate the script 	

              $source  <your-directory>bin/activate

 
    2.3 Once you install python3 and setup environment you are ready to install Django Framework. 
 
            Below is the command to install Django framework
  
      				$pip install django==2
 
          Where no. 2 is version of django. The latest version of Django will also support.
 
 
 



For detailed installation steps  of above pre requities and additional documentation you can reffer the document from below link

https://docs.google.com/document/d/1t3fjkJ0PguogkpHxfY52DTvtfWJPVtj0OVnh3GV2rxk/edit?usp=sharing
