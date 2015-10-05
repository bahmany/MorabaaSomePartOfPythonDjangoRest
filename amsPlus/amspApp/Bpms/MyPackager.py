import io
import os
import zipfile
from SpiffWorkflow.bpmn.storage.Packager import Packager
import xml.etree.ElementTree as ET

class MyPackager(Packager):
    def create_package_xml(self):
        """
        Creates the package, writing the data out to the provided file-like object.
        """

        #Check that all files exist (and calculate the longest shared path prefix):

        #Parse all of the XML:
        self.bpmn={}

        bpmn = ET.parse(io.StringIO(self.input_files[0]))
        self.bpmn=bpmn

        #Now run through pre-parsing and validation:


        #Now check that we can parse it fine:

        self.parser.add_bpmn_xml(bpmn)

        self.wf_spec = self.parser.get_spec(self.entry_point_process)

        #Now package everything:
        self.package_zip = zipfile.ZipFile(self.package_file, "w", compression=zipfile.ZIP_DEFLATED)

        done_files = set()
        for spec in self.wf_spec.get_specs_depth_first():
            filename = spec.file
            if not filename in done_files:
                done_files.add(filename)

                bpmn = self.bpmn
                self.write_to_package_zip("%s.bpmn" % spec.name, ET.tostring(bpmn.getroot()))

                # self.write_file_to_package_zip("src/" + self._get_zip_path(filename), filename)

                self._call_editor_hook('package_for_editor', spec, filename)

        self.write_meta_data()
        self.write_manifest()

        self.package_zip.close()