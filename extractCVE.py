import json
import os

loopCounter = 0000
folderName = ""


for loopCounter in range(7000):
    #0000-0999
    try:
        #with open('aFolder/CVE-2024-0007.json', 'r') as f:
        print("trying to oen folder %d" %(loopCounter))
        with open('aFolder/CVE-2024-%04d.json' % (loopCounter), 'r') as f:
            data = json.load(f)
            cve_id = data["cveMetadata"]["cveId"]

            description = data["containers"]["cna"]["descriptions"][0]["value"]

            datePublished = data["cveMetadata"]["datePublished"]

            dateUpdated = data["cveMetadata"]["dateUpdated"]

            vendor = data["containers"]["cna"]["affected"][0]["vendor"]

            product = data["containers"]["cna"]["affected"][0]["product"]

            # Navigate to the affected versions
            affected_versions = data['containers']['cna']['affected']

            allReferences = data["containers"]["cna"]["references"]

            states = data["cveMetadata"]["state"]


            # Extract all versions
            versions = []
            for affected in affected_versions:
                for version_data in affected['versions']:
                    version = version_data['version']
                    versions.append(version)
            
            versionString = ""
            
            versionCounter = 0
            for version in versions:
                if versionCounter == 0:
                    versionString = version
                    versionCounter = versionCounter+1
                else:
                    versionString + ", " + version




            refString = ''  



            refCounter = 0;
            for ref in allReferences:
                if refCounter == 0:
                    refString = ref["url"]
                    refCounter = refCounter+1
                else:
                    refString + "\n, " + ref["url"]
            


            

            #text_content = f"CVE: {cve_id}\n\n State: {state}\n\n Date Published {datePublished}\n Date Updated {dateUpdated}\n\n Vendor: {vendor}\n\n Product: {product}\n\n Versions: {versionString}\n\n Description: {description}\n\n Refernces: {refString}\n\n\n\n"
            text_content = f"CVE: {cve_id}\n\n State: {states}\n\n Date Published {datePublished}\n Date Updated {dateUpdated}\n\n Vendor: {vendor}\n\n Product: {product}\n\n Description: {description}\n\n Refernces: {refString}\n\n\n\n"

            #write to a text file

            output_file = "cve_description1.txt"
            with open(output_file, 'a') as f:
                f.write(text_content)
                print("placed in")
            # Process data as needed
    except FileNotFoundError:
        print("")

    except KeyError as e:
        try:
            # Attempt to delete the file
            os.remove("CVE-2024-%04d.json" %(loopCounter))
            print("successfully deleted CVE-2024-%04d"%(loopCounter))
        except OSError as e:
            print("Error Deleting")
    except UnicodeDecodeError as e:
        try:
            # Attempt to delete the file
            os.remove("CVE-2024-%04d.json" %(loopCounter))
            print("successfully deleted CVE-2024-%04d"%(loopCounter))
        except OSError as e:
            print("Error Deleting")
    #except Exception as e:
        #print(f"An unexpected error occurred: {e}")
        # Handle other exceptions if necessary

loopCounter2=20000
for loopCounter2 in range(20000,39000):
    #0000-0999
    print (loopCounter2);
    try:
        #with open('aFolder/CVE-2024-0007.json', 'r') as f:
        print("trying to oen folder %d" %(loopCounter2))
        with open('aFolder/CVE-2024-%d.json' % (loopCounter2), 'r') as f:
            data = json.load(f)
            cve_id = data["cveMetadata"]["cveId"]

            description = data["containers"]["cna"]["descriptions"][0]["value"]

            datePublished = data["cveMetadata"]["datePublished"]

            dateUpdated = data["cveMetadata"]["dateUpdated"]

            vendor = data["containers"]["cna"]["affected"][0]["vendor"]

            product = data["containers"]["cna"]["affected"][0]["product"]

            allReferences = data["containers"]["cna"]["references"]

            states = data["cveMetadata"]["state"]



            # Navigate to the affected versions
            affected_versions = data['containers']['cna']['affected']


            # Extract all versions
            versions = []
            for affected in affected_versions:
                for version_data in affected['versions']:
                    version = version_data['version']
                    versions.append(version)
            
            versionString = ""
            
            versionCounter = 0
            for version in versions:
                if versionCounter == 0:
                    versionString = version
                    versionCounter = versionCounter +1
                else:
                    versionString + ", " + version

            refString = ''  



            refCounter = 0;
            for ref in allReferences:
                if refCounter == 0:
                    refString = ref["url"]
                    refCounter = refCounter+1
                else:
                    refString + "\n, " + ref["url"]
            


            

            text_content = f"CVE: {cve_id}\n\n State: {states}\n\n Date Published {datePublished}\n Date Updated {dateUpdated}\n\n Vendor: {vendor}\n\n Product: {product}\n\n Description: {description}\n\n Refernces: {refString}\n\n\n\n"

            #write to a text file

            output_file = "cve_description1.txt"
            with open(output_file, 'a') as f:
                f.write(text_content)
                print("placed in")
            # Process data as needed
    except FileNotFoundError:
        print("")

    except KeyError as e:
        try:
            # Attempt to delete the file
            os.remove("CVE-2024-%04d.json" %(loopCounter2))
            print("successfully deleted CVE-2024-%04d"%(loopCounter2))
        except OSError as e:
            print("Error Deleting")
    except UnicodeDecodeError as e:
        try:
            # Attempt to delete the file
            os.remove("CVE-2024-%04d.json" %(loopCounter2))
            print("successfully deleted CVE-2024-%04d"%(loopCounter2))
        except OSError as e:
            print("Error Deleting")
   

loopCounter = 0000
folderName = ""


for loopCounter in range(7000):
    #0000-0999
    try:
        #with open('aFolder/CVE-2024-0007.json', 'r') as f:
        print("trying to oen folder %d" %(loopCounter))
        with open('aFolder/CVE-2023-%04d.json' % (loopCounter), 'r') as f:
            data = json.load(f)
            cve_id = data["cveMetadata"]["cveId"]

            description = data["containers"]["cna"]["descriptions"][0]["value"]

            datePublished = data["cveMetadata"]["datePublished"]

            dateUpdated = data["cveMetadata"]["dateUpdated"]

            vendor = data["containers"]["cna"]["affected"][0]["vendor"]

            product = data["containers"]["cna"]["affected"][0]["product"]
            
            # Navigate to the affected versions
            affected_versions = data['containers']['cna']['affected']

            allReferences = data["containers"]["cna"]["references"]

            states = data["cveMetadata"]["state"]
            
# Extract all versions
            versions = []
            for affected in affected_versions:
                for version_data in affected['versions']:
                    version = version_data['version']
                    versions.append(version)
            
            versionString = ""
            
            versionCounter = 0
            for version in versions:
                if versionCounter == 0:
                    versionString = version
                    versionCounter = versionCounter +1
                else:
                    versionString + ", " + version
            

            refString = ''  



            refCounter = 0;
            for ref in allReferences:
                if refCounter == 0:
                    refString = ref["url"]
                    refCounter = refCounter+1
                else:
                    refString + "\n, " + ref["url"]
            


            

            text_content = f"CVE: {cve_id}\n\n State: {states}\n\n Date Published {datePublished}\n Date Updated {dateUpdated}\n\n Vendor: {vendor}\n\n Product: {product}\n\n Description: {description}\n\n Refernces: {refString}\n\n\n\n"

            #write to a text file

            output_file = "cve_description1.txt"
            with open(output_file, 'a') as f:
                f.write(text_content)
                print("placed in")
            # Process data as needed
    except FileNotFoundError:
        print("")

    except KeyError as e:
        try:
            # Attempt to delete the file
            os.remove("CVE-2023-%04d.json" %(loopCounter))
            print("successfully deleted CVE-2023-%04d"%(loopCounter))
        except OSError as e:
            print("Error Deleting")
    except UnicodeDecodeError as e:
        try:
            # Attempt to delete the file
            os.remove("CVE-2023-%04d.json" %(loopCounter))
            print("successfully deleted CVE-2023-%04d"%(loopCounter))
        except OSError as e:
            print("Error Deleting")
    #except Exception as e:
        #print(f"An unexpected error occurred: {e}")
        # Handle other exceptions if necessary

loopCounter2=20000
for loopCounter2 in range(20000,53000):
    #0000-0999
    print (loopCounter2);
    try:
        #with open('aFolder/CVE-2024-0007.json', 'r') as f:
        print("trying to oen folder %d" %(loopCounter2))
        with open('aFolder/CVE-2023-%d.json' % (loopCounter2), 'r') as f:
            data = json.load(f)
            cve_id = data["cveMetadata"]["cveId"]

            description = data["containers"]["cna"]["descriptions"][0]["value"]

            datePublished = data["cveMetadata"]["datePublished"]

            dateUpdated = data["cveMetadata"]["dateUpdated"]

            vendor = data["containers"]["cna"]["affected"][0]["vendor"]

            product = data["containers"]["cna"]["affected"][0]["product"]

            states = data["cveMetadata"]["state"]
            

            # Navigate to the affected versions
            affected_versions = data['containers']['cna']['affected']

            

            # Extract all versions
            versions = []
            for affected in affected_versions:
                for version_data in affected['versions']:
                    version = version_data['version']
                    versions.append(version)
            
            versionString = ""
            
            versionCounter = 0
            for version in versions:
                if versionCounter == 0:
                    versionString = version
                    versionCounter = versionCounter+1
                else:
                    versionString + ", " + version
            

            refString = ''  



            refCounter = 0;
            for ref in allReferences:
                if refCounter == 0:
                    refString = ref["url"]
                    refCounter = refCounter+1
                else:
                    refString + "\n, " + ref["url"]
            


            

            text_content = f"CVE: {cve_id}\n\n State: {states}\n\n Date Published {datePublished}\n Date Updated {dateUpdated}\n\n Vendor: {vendor}\n\n Product: {product}\n\n Description: {description}\n\n Refernces: {refString}\n\n\n\n"
            #write to a text file

            output_file = "cve_description1.txt"
            with open(output_file, 'a') as f:
                f.write(text_content)
                print("placed in")
            # Process data as needed
    except FileNotFoundError:
        print("")

    except KeyError as e:
        try:
            # Attempt to delete the file
            os.remove("CVE-2023-%04d.json" %(loopCounter2))
            print("successfully deleted CVE-2023-%04d"%(loopCounter2))
        except OSError as e:
            print("Error Deleting")
    except UnicodeDecodeError as e:
        try:
            # Attempt to delete the file
            os.remove("CVE-2023-%04d.json" %(loopCounter2))
            print("successfully deleted CVE-2023-%04d"%(loopCounter2))
        except OSError as e:
            print("Error Deleting")


############################################################################

loopCounter = 0000



for loopCounter in range(5000):
    #0000-0999
    try:
        #with open('aFolder/CVE-2024-0007.json', 'r') as f:
        print("trying to oen folder %d" %(loopCounter))
        with open('aFolder/CVE-2022-%04d.json' % (loopCounter), 'r') as f:
            data = json.load(f)
            cve_id = data["cveMetadata"]["cveId"]

            description = data["containers"]["cna"]["descriptions"][0]["value"]

            datePublished = data["cveMetadata"]["datePublished"]

            dateUpdated = data["cveMetadata"]["dateUpdated"]

            vendor = data["containers"]["cna"]["affected"][0]["vendor"]

            product = data["containers"]["cna"]["affected"][0]["product"]

            # Navigate to the affected versions
            affected_versions = data['containers']['cna']['affected']

            allReferences = data["containers"]["cna"]["references"]

            states = data["cveMetadata"]["state"]

            # Extract all versions
            versions = []
            for affected in affected_versions:
                for version_data in affected['versions']:
                    version = version_data['version']
                    versions.append(version)
            
            versionString = ""
            
            versionCounter = 0
            for version in versions:
                if versionCounter == 0:
                    versionString = version
                    versionCounter = versionCounter+1
                else:
                    versionString + ", " + version
            

            refString = ''  



            refCounter = 0;
            for ref in allReferences:
                if refCounter == 0:
                    refString = ref["url"]
                    refCounter = refCounter+1
                else:
                    refString + "\n, " + ref["url"]
            


            

            text_content = f"CVE: {cve_id}\n\n State: {states}\n\n Date Published {datePublished}\n Date Updated {dateUpdated}\n\n Vendor: {vendor}\n\n Product: {product}\n\n Description: {description}\n\n Refernces: {refString}\n\n\n\n"

            #write to a text file

            output_file = "cve_description1.txt"
            with open(output_file, 'a') as f:
                f.write(text_content)
                print("placed in")
            # Process data as needed
    except FileNotFoundError:
        print("")

    except KeyError as e:
        try:
            # Attempt to delete the file
            os.remove("CVE-2022-%04d.json" %(loopCounter))
            print("successfully deleted CVE-2022-%04d"%(loopCounter))
        except OSError as e:
            print("Error Deleting")
    except UnicodeDecodeError as e:
        try:
            # Attempt to delete the file
            os.remove("CVE-2022-%04d.json" %(loopCounter))
            print("successfully deleted CVE-2022-%04d"%(loopCounter))
        except OSError as e:
            print("Error Deleting")
    #except Exception as e:
        #print(f"An unexpected error occurred: {e}")
        # Handle other exceptions if necessary

loopCounter2=20000
for loopCounter2 in range(20000,49000):
    #0000-0999
    print (loopCounter2);
    try:
        #with open('aFolder/CVE-2024-0007.json', 'r') as f:
        print("trying to oen folder %d" %(loopCounter2))
        with open('aFolder/CVE-2022-%d.json' % (loopCounter2), 'r') as f:
            data = json.load(f)
            cve_id = data["cveMetadata"]["cveId"]

            description = data["containers"]["cna"]["descriptions"][0]["value"]

            datePublished = data["cveMetadata"]["datePublished"]

            dateUpdated = data["cveMetadata"]["dateUpdated"]

            vendor = data["containers"]["cna"]["affected"][0]["vendor"]

            product = data["containers"]["cna"]["affected"][0]["product"]

            # Navigate to the affected versions
            affected_versions = data['containers']['cna']['affected']

            allReferences = data["containers"]["cna"]["references"]

            states = data["cveMetadata"]["state"]

            # Extract all versions
            versions = []
            for affected in affected_versions:
                for version_data in affected['versions']:
                    version = version_data['version']
                    versions.append(version)
            
            versionString = ""
            
            versionCounter = 0
            for version in versions:
                if versionCounter == 0:
                    versionString = version
                    versionCounter = versionCounter+1
                else:
                    versionString + ", " + version
            

            refString = ''  



            refCounter = 0;
            for ref in allReferences:
                if refCounter == 0:
                    refString = ref["url"]
                    refCounter = refCounter+1
                else:
                    refString + "\n, " + ref["url"]
            


            

            text_content = f"CVE: {cve_id}\n\n State: {states}\n\n Date Published {datePublished}\n Date Updated {dateUpdated}\n\n Vendor: {vendor}\n\n Product: {product}\n\n Description: {description}\n\n Refernces: {refString}\n\n\n\n"

            #write to a text file

            output_file = "cve_description1.txt"
            with open(output_file, 'a') as f:
                f.write(text_content)
                print("placed in")
            # Process data as needed
    except FileNotFoundError:
        print("")

    except KeyError as e:
        try:
            # Attempt to delete the file
            os.remove("CVE-2022-%04d.json" %(loopCounter2))
            print("successfully deleted CVE-2022-%04d"%(loopCounter2))
        except OSError as e:
            print("Error Deleting")
    except UnicodeDecodeError as e:
        try:
            # Attempt to delete the file
            os.remove("CVE-2022-%04d.json" %(loopCounter2))
            print("successfully deleted CVE-2022-%04d"%(loopCounter2))
        except OSError as e:
            print("Error Deleting")



########################################################################

loopCounter = 0000



for loopCounter in range(5000):
    #0000-0999
    try:
        #with open('aFolder/CVE-2024-0007.json', 'r') as f:
        print("trying to oen folder %d" %(loopCounter))
        with open('aFolder/CVE-2021-%04d.json' % (loopCounter), 'r') as f:
            data = json.load(f)
            cve_id = data["cveMetadata"]["cveId"]

            description = data["containers"]["cna"]["descriptions"][0]["value"]

            datePublished = data["cveMetadata"]["datePublished"]

            dateUpdated = data["cveMetadata"]["dateUpdated"]

            vendor = data["containers"]["cna"]["affected"][0]["vendor"]

            product = data["containers"]["cna"]["affected"][0]["product"]

            # Navigate to the affected versions
            affected_versions = data['containers']['cna']['affected']

            allReferences = data["containers"]["cna"]["references"]
            
            states = data["cveMetadata"]["state"]

            # Extract all versions
            versions = []
            for affected in affected_versions:
                for version_data in affected['versions']:
                    version = version_data['version']
                    versions.append(version)
            
            versionString = ""
            
            versionCounter = 0
            for version in versions:
                if versionCounter == 0:
                    versionString = version
                    versionCounter = versionCounter+1
                else:
                    versionString + ", " + version
            

            refString = ''  



            refCounter = 0;
            for ref in allReferences:
                if refCounter == 0:
                    refString = ref["url"]
                    refCounter = refCounter+1
                else:
                    refString + "\n, " + ref["url"]
            


            

            text_content = f"CVE: {cve_id}\n\n State: {states}\n\n Date Published {datePublished}\n Date Updated {dateUpdated}\n\n Vendor: {vendor}\n\n Product: {product}\n\n Description: {description}\n\n Refernces: {refString}\n\n\n\n"

            #write to a text file

            output_file = "cve_description1.txt"
            with open(output_file, 'a') as f:
                f.write(text_content)
                print("placed in")
            # Process data as needed
    except FileNotFoundError:
        print("")

    except KeyError as e:
        try:
            # Attempt to delete the file
            os.remove("CVE-2021-%04d.json" %(loopCounter))
            print("successfully deleted CVE-2021-%04d"%(loopCounter))
        except OSError as e:
            print("Error Deleting")
    except UnicodeDecodeError as e:
        try:
            # Attempt to delete the file
            os.remove("CVE-2021-%04d.json" %(loopCounter))
            print("successfully deleted CVE-2021-%04d"%(loopCounter))
        except OSError as e:
            print("Error Deleting")
    #except Exception as e:
        #print(f"An unexpected error occurred: {e}")
        # Handle other exceptions if necessary

loopCounter2=20000
for loopCounter2 in range(20000,48000):
    #0000-0999
    print (loopCounter2);
    try:
        #with open('aFolder/CVE-2024-0007.json', 'r') as f:
        print("trying to oen folder %d" %(loopCounter2))
        with open('aFolder/CVE-2021-%d.json' % (loopCounter2), 'r') as f:
            data = json.load(f)
            cve_id = data["cveMetadata"]["cveId"]

            description = data["containers"]["cna"]["descriptions"][0]["value"]

            datePublished = data["cveMetadata"]["datePublished"]

            dateUpdated = data["cveMetadata"]["dateUpdated"]

            vendor = data["containers"]["cna"]["affected"][0]["vendor"]

            product = data["containers"]["cna"]["affected"][0]["product"]

            # Navigate to the affected versions
            affected_versions = data['containers']['cna']['affected']

            allReferences = data["containers"]["cna"]["references"]

            states = data["cveMetadata"]["state"]

            # Extract all versions
            versions = []
            for affected in affected_versions:
                for version_data in affected['versions']:
                    version = version_data['version']
                    versions.append(version)
            
            versionString = ""
            
            versionCounter = 0
            for version in versions:
                if versionCounter == 0:
                    versionString = version
                    versionCounter = versionCounter+1
                else:
                    versionString + ", " + version
            

            refString = ''  



            refCounter = 0;
            for ref in allReferences:
                if refCounter == 0:
                    refString = ref["url"]
                    refCounter = refCounter+1
                else:
                    refString + "\n, " + ref["url"]
            


            

            text_content = f"CVE: {cve_id}\n\n State: {states}\n\n Date Published {datePublished}\n Date Updated {dateUpdated}\n\n Vendor: {vendor}\n\n Product: {product}\n\n Description: {description}\n\n Refernces: {refString}\n\n\n\n"

            #write to a text file

            output_file = "cve_description1.txt"
            with open(output_file, 'a') as f:
                f.write(text_content)
                print("placed in")
            # Process data as needed
    except FileNotFoundError:
        print("")

    except KeyError as e:
        try:
            # Attempt to delete the file
            os.remove("CVE-2021-%04d.json" %(loopCounter2))
            print("successfully deleted CVE-2021-%04d"%(loopCounter2))
        except OSError as e:
            print("Error Deleting")
    except UnicodeDecodeError as e:
        try:
            # Attempt to delete the file
            os.remove("CVE-2021-%04d.json" %(loopCounter2))
            print("successfully deleted CVE-2021-%04d"%(loopCounter2))
        except OSError as e:
            print("Error Deleting")