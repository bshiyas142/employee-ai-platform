class PromptBuilder:

    @staticmethod
    def employee_summary(employee) ->str:
        return f"""Summarize this employee professionally.
        Employee Id: {employee.employee_id}
        Name: {employee.first_name} {employee.last_name}
        Department ID: {employee.department_id}
        Designation: {employee.designation.value}

        Provide concise Summary."""


    @staticmethod
    def employee_query(question: str) -> str:
        return f""" Convert the user's question into a structured query for employee data.
        User question: {question}
        Rules:
            - operation: one of "LIST", "GET", or "COUNT"
            - use LIST for queries that request multiple employees, GET for a specific employee, and COUNT for counting employees.
            - The query should be concise and only include relevant fields based on the user's question.
            - The query should not include any additional text or explanatioin.
            - Dates must be in the format YYYY-MM-DD.

        
        
        """

        