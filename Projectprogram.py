import ProjectClass as p

inst1 = p.Project(1001, 'SAP Implementation', 25, '09/30/2022')

inst2 = p.Project(1002, 'Migration to CRM', 10, '06/30/2022')

projectdict = {inst1.get_projID(): inst1.get_dueDate(),
               inst2.get_projID(): inst2.get_dueDate()}

print(projectdict)

