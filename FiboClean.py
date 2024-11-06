from manim import *
import os

config.frame_height = 1000
config.frame_width = 1200


class FibonacciWithAddition(Scene):
    def construct(self):
        # Fibonacci sequence values to generate
        fib_numbers = [1, 1, 2, 3, 5, 8, 13, 21]
        
        # Start with the first two Fibonacci numbers
        start_position = LEFT * 4
        numbers = [Text("1", font_size=36), Text("1", font_size=36)]
        
        # Position the initial two numbers
        numbers[0].move_to(start_position)
        numbers[1].move_to(start_position + RIGHT)
        
        # Display the first two numbers
        self.play(FadeIn(numbers[0]), FadeIn(numbers[1]))

        # Loop to create Fibonacci numbers dynamically
        for i in range(2, len(fib_numbers)):
            # Create brace under the last two numbers
            brace = Brace(VGroup(numbers[i-2], numbers[i-1]), UP).set_color(GOLD)
            
            # Copy the last two numbers and move them upwards
            first_copy = numbers[i-2].copy()
            second_copy = numbers[i-1].copy()
            plus = Text("+", font_size=36)
            
            first_copy.move_to(numbers[i-2].get_center() + UP )
            second_copy.move_to(numbers[i-1].get_center() + UP)
            plus.move_to((first_copy.get_center() + second_copy.get_center()) / 2)
            
            self.play(FadeIn(brace), TransformFromCopy(numbers[i-2], first_copy), TransformFromCopy(numbers[i-1], second_copy))
            self.play(FadeIn(plus))
            
            # Create the resulting sum number
            sum_result = Text(str(fib_numbers[i]), font_size=36)
            sum_result.move_to(plus.get_center())
            
            # Transform the two numbers and plus sign into the sum result
            self.play(ReplacementTransform(first_copy, sum_result), FadeOut(second_copy), FadeOut(plus))
            
            
            # Move the sum result down to its correct position in the sequence
            self.play(
                sum_result.animate.next_to(numbers[i-1], RIGHT, buff=1)
            )
            
            # Add the new number to the sequence
            numbers.append(sum_result)
            
            self.play(FadeOut(brace))
            brace.next_to(VGroup(numbers[i-1], sum_result), UP)
            if (i == len(fib_numbers) -1):
                dots = Text("...", font_size = 36).next_to(sum_result, RIGHT, buff = 1)
                self.play(Write(dots))
            # Move the brace to the new last two numbers          
            # Fade out the brace for the next iteration
        
        # Hold the final scene for a moment
        self.wait(2)



class FibonacciFormalDefinition(Scene):
    def construct(self):
        # Title
        title = Text("Fibonacci Function").scale(1.2).to_edge(UP)
        self.play(Write(title))

        # Define individual equations with conditions
        #equation_1 = MathTex(r"0 \quad & \text{if } n = 0").scale(1.2)
        equation_2 = MathTex(r"1 \quad & \text{if } n = 0 \text{ or } n = 1").scale(1.2)
        equation_3 = MathTex(r"F(n-1) + F(n-2) \quad & \text{if } n \geq 2").scale(1.2)

        # Align initial equations vertically
        #equation_1.move_to(DOWN * 1.5)
        equation_2.move_to(DOWN * 1.5)
        equation_3.next_to(equation_2, DOWN, aligned_edge=LEFT)

        brace = Brace(VGroup(equation_2, equation_3), LEFT)

        # Create the F(n) = text and position it next to the brace
        fib_text = MathTex(r"F(n) =").scale(1.2).next_to(brace, LEFT, buff=0.1)

        self.play(Write(fib_text))
        self.play(Create(brace))
        # Add equations to the scene
        #self.play(Write(equation_1))
        self.play(Write(equation_2))
        self.play(Write(equation_3))
        # Add some pauses for clarity
        self.wait(2)



class ShowFibonacciCode(Scene):
    def construct(self):
        title = Text("Fibonacci Computation using Recursion", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        # Create a Code object with the Fibonacci recursive algorithm
        code = Code(
            code="""
                def fiboRec(n):
                    if n <= 1:
                        return 1
                    else:
                        return fiboRec(n-1) + fiboRec(n-2)
            """,
            tab_width=4,
            background="window",
            language="Python",
            font="Monospace",
        )
        
        # Center the code on the screen
        code.scale(0.75).move_to(ORIGIN)

        # Add the code to the scene and display it
        self.play(Write(code))
        self.wait(3)


class FibonacciRecursionTree(Scene):
    def construct(self):
        # Title

        # Recursion tree for F(4)
        tree_title = Text("Recursion Tree for F(4)", font_size=36)
        self.play(Write(tree_title))
        self.wait(2)
        self.play(FadeOut(tree_title))

        # Define the positions of the nodes
        positions = {
            "F4": [0, 3, 0],
            "F3L": [-3, 1.5, 0],
            "F3R": [3, 1.5, 0],
            "F2LL": [-5, 0, 0],
            "F2LR": [-1, 0, 0],
            "F2RL": [1, 0, 0],
            "F2RR": [5, 0, 0],
            "F1LLL": [-6, -1.5, 0],
            "F1LLR": [-4, -1.5, 0],
            "F1LRL": [-2, -1.5, 0],
            "F0LRR": [0, -1.5, 0],
            "F1RRL": [4, -1.5, 0],
            "F0RRR": [6, -1.5, 0]
        }

        # # Create the nodes
        # nodes = {
        #     "F4": Text("F(n)").move_to(positions["F4"]),
        #     "F3L": Text("F(n-1)").move_to(positions["F3L"]),
        #     "F3R": Text("F(n-2)").move_to(positions["F3R"]),
        #     "F2LL": Text("F(n-2)").move_to(positions["F2LL"]),
        #     "F2LR": Text("F(n-3)").move_to(positions["F2LR"]),
        #     "F2RL": Text("F(n-3)").move_to(positions["F2RL"]),
        #     "F2RR": Text("F(n-4)").move_to(positions["F2RR"]),
        #     "F1LLL": Text("F(n-3)").move_to(positions["F1LLL"]),
        #     "F1LLR": Text("F(n-4)").move_to(positions["F1LLR"]),
        #     "F1LRL": Text("F(n-4)").move_to(positions["F1LRL"]),
        #     "F0LRR": Text("F(n-5)").move_to(positions["F0LRR"]),
        #     "F1RRL": Text("...").move_to(positions["F1RRL"]),
        #     "F0RRR": Text("...").move_to(positions["F0RRR"]),
        # }
        FS = 29
        nodes = {
            "F4": Text("F(n)", font_size=FS).move_to(positions["F4"]),
            "F3L": Text("F(n-1)", font_size=FS).move_to(positions["F3L"]),
            "F3R": Text("F(n-2)", font_size=FS).move_to(positions["F3R"]),
            "F2LL": Text("F(n-2)", font_size=FS).move_to(positions["F2LL"]),
            "F2LR": Text("F(n-3)", font_size=FS).move_to(positions["F2LR"]),
            "F2RL": Text("F(n-3)", font_size=FS).move_to(positions["F2RL"]),
            "F2RR": Text("F(n-4)", font_size=FS).move_to(positions["F2RR"]),
            "F1LLL": Text("F(n-3)", font_size=FS).move_to(positions["F1LLL"]),
            "F1LLR": Text("F(n-4)", font_size=FS).move_to(positions["F1LLR"]),
            "F1LRL": Text("F(n-4)", font_size=FS).move_to(positions["F1LRL"]),
            "F0LRR": Text("F(n-5)", font_size=FS).move_to(positions["F0LRR"]),
            "F1RRL": Text("...", font_size=FS).move_to(positions["F1RRL"]),
            "F0RRR": Text("...", font_size=FS).move_to(positions["F0RRR"]),
        }

        # Create the edges
        edges = [
            ("F4", "F3L"), ("F4", "F3R"),
            ("F3L", "F2LL"), ("F3L", "F2LR"),
            ("F3R", "F2RL"), ("F3R", "F2RR"),
            ("F2LL", "F1LLL"), ("F2LL", "F1LLR"),
            ("F2LR", "F1LRL"), ("F2LR", "F0LRR"),
            #("F2RL", "F1RRL"), ("F2RR", "F0RRR")
        ]

        # Progressive display of the tree
        def show_tree(nodes, edges):
            #for node_key in nodes:
            faded = []
            for start, end in edges:
                if (start not in faded):
                    self.play(FadeIn(nodes[start]))
                    faded.append(start)

                self.wait(0.5)
                line = Line(nodes[start].get_bottom(), nodes[end].get_top())
                self.play(Write(line))
                self.wait(0.5)
                if (end not in faded):
                    self.play(FadeIn(nodes[end]))
                    faded.append(end)

            dots = Text("...").move_to([4, -1.5, 0])
            self.play(Write(dots))


        show_tree(nodes, edges)

        left_node = nodes["F2RL"]
        right_node = nodes["F2RR"]

        # Define the points for the triangle vertices
        top_vertex1 = nodes["F3R"].get_top() + UP * 0.5  # A little above F(n-2)
        left_vertex1= left_node.get_left() + LEFT  + 0.3*DOWN 
        right_vertex1 = right_node.get_right() + RIGHT + 0.3*DOWN

        # Create and draw the triangle
        redundancy_triangle1 = Polygon(top_vertex1, left_vertex1, right_vertex1, stroke_width = 0, color=RED, fill_color=BLUE, fill_opacity = 0.3)
        #redundancy_triangle1P = Polygon(top_vertex1, left_vertex1 + DOWN, right_vertex1 + DOWN, stroke_width = 0,  color=BLUE, fill_color=BLUE, fill_opacity = 0.1)


        left_node2 = nodes["F1LLL"]
        right_node2 = nodes["F1LLR"]

        # Define the points for the triangle vertices
        top_vertex2 = nodes["F2LL"].get_top() + UP * 0.5  # A little above F(n-2)
        left_vertex2= left_node2.get_left() + LEFT * 0.5 + 0.3* DOWN 
        right_vertex2 = right_node2.get_right() + RIGHT * 0.5 + 0.3* DOWN

        # Create and draw the triangle
        redundancy_triangle2 = Polygon(top_vertex2, left_vertex2, right_vertex2, stroke_width = 0, color=RED, fill_color=BLUE, fill_opacity = 0.3)
        #redundancy_triangle1P = Polygon(top_vertex1, left_vertex1 + DOWN, right_vertex1 + DOWN, stroke_width = 0,  color=BLUE, fill_color=BLUE, fill_opacity = 0.1)


        self.wait(5)

        self.play(Write(redundancy_triangle1))

        #self.wait(2)
        self.play(Write(redundancy_triangle2))
        self.wait(2)
        # # Complexity analysis
        # #complexity_text = Tex("Time Complexity: $O(2^n)$", font_size=36).move_to()
        # self.play(Write(complexity_text))
        # self.wait(3)
        # self.play(FadeOut(complexity_text))

        # # Summary
        # summary = Text("Exponential growth due to redundant calculations", font_size=36)
        # self.play(Write(summary))
        # self.wait(3)
        # self.play(FadeOut(summary))



class FibonacciMemoization(Scene):
    def construct(self):
        # Title
        title = Text("Fibonacci Computation using Memoization", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Explanation of Memoization
        explanation = Text(
            "Memoization stores previously computed values\n"
            "to avoid redundant calculations.",
            font_size=36
        )
        self.play(Write(explanation))
        self.wait(3)
        self.play(FadeOut(explanation))

        # Memoized Fibonacci function definition
        fib_code = """
            def fib_memo(n, memo={}):
                if n in memo:
                    return memo[n]
                if n <= 1:
                    memo[n] = 1
                else:
                    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
                return memo[n]
            """
        code = Code(code=fib_code, language="Python", font="Monospace", background="window")
        self.play(FadeIn(code))
        self.wait(3)
        self.play(FadeOut(code))

        # Memoization table
        table_title = Text("Memoization Table for F(7)", font_size=36)
        self.play(Write(table_title))
        self.wait(2)
        self.play(FadeOut(table_title))

        # Create a table for memoization
        table = Table(
            [["n", "0", "1", "2", "3", "4", "5", "6", "7"],
             ["F(n)", "1", "1", "", "", "", "", "", ""]],
            include_outer_lines=True
        ).scale(0.8).to_edge(UP)
        self.play(Create(table))
        self.wait(2)

        # Function to update the table
        def update_table(row, col, value):
            cell = table.get_cell((row, col))
            cell2 = table.get_cell((row, col -2))
            cell1 = table.get_cell((row, col-1))
            cells =  VGroup(cell1, cell2)

            new_text = Text(value, font_size=36).move_to(cell.get_center())
            self.play(Transform(cells, new_text))
            self.wait(1)

        # Fill the memoization table progressively
        update_table(2, 4, "2")
        update_table(2, 5, "3")
        update_table(2, 6, "5")
        update_table(2, 7, "8")
        update_table(2, 8, "13")
        update_table(2, 9, "21")

        # Complexity analysis
        complexity_text = Tex("Time Complexity: $O(n)$\nSpace Complexity: $O(n)$", font_size=36)
        self.play(Write(complexity_text))
        self.wait(3)
        self.play(FadeOut(complexity_text))

        # Summary
        summary = Text("Linear growth due to stored intermediate results", font_size=36)
        self.play(Write(summary))
        self.wait(3)
        #self.play(FadeOut(summary), FadeOut(table))



class FibonacciWithTempVariableII(Scene):
    def construct(self):
        # Title
        title = Text("Fibonacci Calculation Using Temporary Variable", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Explanation
        explanation = Text(
            "Using variables a, b, and temp to store intermediate values.",
            font_size=36
        )
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(explanation))


        # Display the Fibonacci function code
        fib_code = """
            def fib(n):
                if n <= 1:
                    return n
                a, b = 1, 1
                for _ in range(2, n + 1):
                    temp = a + b  
                    a = b
                    b = temp 
                return b
        """
        code_display = Code(
            code=fib_code, language="Python", font="Monospace", background="window"
        )
        self.play(FadeIn(code_display))
        self.wait(3)
        self.play(code_display.animate.shift(5*LEFT))
        #self.play(FadeOut(code_display))

        # Display initial values of a and b
        a_old = Text("a = 1", font_size=36, color=BLUE).shift(2*RIGHT + 0 * UP)
        b_old = Text("b = 1", font_size=36, color=GREEN).shift(2*RIGHT + 1 * DOWN)
        temp_old = Text("temp = -", font_size=36, color=GRAY).shift(2*RIGHT + 1 * UP)


        self.play(Write(temp_old))
        self.play(Write(a_old))
        self.play(Write(b_old))
        self.wait(2)

        # Initialize the Fibonacci values and simulate the update steps
        a, b = 1, 1  # Starting values F(0) = 0 and F(1) = 1
        for i in range(2, 9):  # Compute up to F(8)
            # Calculate the next Fibonacci value
            temp = a + b

            # Display new values for a, b, and temp
            a_new = Text(f"a = {b}", font_size=36, color=BLUE).next_to(a_old, 0*DOWN, buff=1)
            b_new = Text(f"b = {temp}", font_size=36, color=GREEN).next_to(b_old, 0*DOWN, buff=1)
            temp_new = Text(f"temp = {temp}", font_size=36, color=ORANGE).next_to(temp_old, 0*DOWN, buff=1)

            # Show calculation step

            self.play(Transform(temp_old, temp_new))
            self.play(Transform(a_old, a_new))
            self.play(Transform(b_old, b_new))

            self.wait(2)

            # Update old values to new values by shifting them up
            # self.play(a_old.animate.become(a_new))
            # self.play(b_old.animate.become(b_new))
            # self.play(temp_old.animate.become(temp_new))

            # Update the variables in Python for the next iteration
            a, b = b, temp


        self.play(FadeOut(code_display), FadeOut(temp_new), FadeOut(a_new), FadeOut(b_new), FadeOut(a_old), FadeOut(b_old), FadeOut(temp_old))
        # Complexity Analysis
        complexity_text = Tex("Time Complexity: $O(n)$\nSpace Complexity: $O(1)$", font_size=36)
        self.play(Write(complexity_text))
        self.wait(3)
        self.play(FadeOut(complexity_text))

        # Summary
        summary = Text(
            "The algorithm uses only two variables for the last two values\n"
            "and a temporary variable for intermediate results, optimizing space usage.",
            font_size=36
        )
        self.play(Write(summary))
        self.wait(3)
        self.play(FadeOut(summary))

class MatrixMultiplicationFibonacci(Scene):
    def construct(self):
        #f = self.camera.frame
        # Title
        # title = Text("Matrix Multiplication in Fibonacci", font_size=48)
        # self.play(Write(title))
        # self.wait(2)
        # self.play(FadeOut(title))

        # Matrix and vector to be multiplied
        matrix = MathTex(r"\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}", font_size=60)
        vector = MathTex(r"\begin{pmatrix} F(n-1) \\ F(n-2) \end{pmatrix}", font_size=60)
        equals = MathTex(r"=", font_size=60)
        result = MathTex(r"\begin{pmatrix} F(n) \\ F(n-1) \end{pmatrix}", font_size=60)

        # Arrange the matrix and vectors
        result.shift(LEFT * 3)
        equals.next_to(result, RIGHT)
        matrix.next_to(equals, RIGHT)
        vector.next_to(matrix, RIGHT)

        # Show the equation on the screen
        self.play(Write(result))
        self.wait(1)
        self.play(Write(matrix), Write(vector), Write(equals))
        self.wait(2)

        # Yellow rectangle to highlight parts of the matrix and vector
        rect_result_1 = SurroundingRectangle(result[0][1:5], color=YELLOW)
        rect_matrix_1_1 = SurroundingRectangle(matrix[0][1:3], color=YELLOW)
        rect_vector_1 = SurroundingRectangle(vector[0][1:12], color=YELLOW)


        # # Step 1: Show multiplication for the first row, first column
        self.play(Create(rect_matrix_1_1), Create(rect_vector_1), Create(rect_result_1))
        multiplication_text_1 = MathTex(r"F(n) = 1 \cdot F(n-1) + 1 \cdot F(n-2)", font_size=36)
        multiplication_text_1.next_to(equals, 6*DOWN)

        self.play(Write(multiplication_text_1))
        self.wait(2)
        self.play(FadeOut(rect_matrix_1_1), FadeOut(rect_vector_1), FadeOut(rect_result_1))

        # Yellow rectangles for the second part (second row and column)
        rect_result_2 = SurroundingRectangle(result[0][5:11], color=YELLOW)
        rect_matrix_2_1 = SurroundingRectangle(matrix[0][3:5], color=YELLOW)
        rect_vector_2 = SurroundingRectangle(vector[0][1:12], color=YELLOW)

        # Step 2: Show multiplication for the second row, first column
        self.play(Create(rect_matrix_2_1), Create(rect_vector_2), Create(rect_result_2))
        multiplication_text_2 = MathTex(r"F(n-1) = 1 \cdot F(n-1) + 0 \cdot F(n-2)", font_size=36)
        multiplication_text_2.next_to(multiplication_text_1, DOWN)

        self.play(Write(multiplication_text_2))
        self.wait(2)

        # Fade out the yellow rectangles and cleanup
        self.play(FadeOut(rect_matrix_2_1), FadeOut(rect_vector_2), FadeOut(rect_result_2))
        self.play(FadeOut(multiplication_text_1), FadeOut(multiplication_text_2))


        matrix2 = MathTex(r"\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}", font_size=60)
        vector2 = MathTex(r"\begin{pmatrix} F(n-2) \\ F(n-3) \end{pmatrix}", font_size=60)
        equals2 = MathTex(r"=", font_size=60)

        # Arrange the matrix and vectors
        #result.shift(LEFT * 3)
        equals2.next_to(matrix, RIGHT + 3*DOWN)
        matrix2.next_to(equals2, RIGHT)
        vector2.next_to(matrix2, RIGHT)

        self.play(Write(equals2))
        self.wait(1)
        self.play(Write(matrix2), Write(vector2))
        self.wait(2)
        self.play(FadeOut(equals2),FadeOut(vector), matrix2.animate.shift(1.5*UP), vector2.animate.shift(1.5*UP))
        self.wait(2)
        matrixP2 = MathTex(r"\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^2", font_size=60).next_to(equals, RIGHT)
        VG = VGroup(matrix, matrix2)
        self.play(TransformMatchingShapes(VG, matrixP2))
        self.play(vector2.animate.shift(2*LEFT))

        MPo = matrixP2
        self.play(Transform(matrixP2, MPo))
        MPn = matrixP2

        MVo = vector2
        self.play(Transform(vector2, MVo))
        MVn = MVo
        n = 9
        for i in range(3,n):
            MPn = MathTex(r"\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^{" + str(i) + "}", font_size=60).next_to(equals, RIGHT)
            MVn = MathTex(r"\begin{pmatrix} F(n-{" + str(i) + r"}) \\ F(n-{" + str(i+1) + r"}) \end{pmatrix}", font_size=60).next_to(MPn, RIGHT)
            self.play(TransformMatchingShapes(MPo, MPn), ReplacementTransform(MVo, MVn))
            MPo = MPn
            MVo = MVn
            if (i == 3):
                self.wait(2)


        MPn = MathTex(r"\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n", font_size=60).next_to(equals, RIGHT)
        MVn = MathTex(r"\begin{pmatrix} F(1) \\ F(0) \end{pmatrix}", font_size=60).next_to(MPn, RIGHT)
        self.play(TransformMatchingShapes(MPo, MPn), ReplacementTransform(MVo, MVn))
        self.wait(2)
        MVnL = MathTex(r"\begin{pmatrix} 1 \\ 1 \end{pmatrix}", font_size=60).next_to(MPn, RIGHT)
        self.play(ReplacementTransform(MVn, MVnL))
        self.wait(3)


        brace = Brace(MPn, DOWN)

        # Add the label "Complexity of O(log2n)" in yellow
        complexity_label = Tex(r"Complexity of $O(\log_2 n)$", color=YELLOW).next_to(brace, DOWN)
        
        # Add another label below for "Fast Exponentiation" in blue
        method_label = Tex(r"using Fast Exponentiation", color=BLUE).next_to(complexity_label, DOWN)

        # Animate the creation of the brace and the labels
        self.play(Create(brace))
        self.play(Write(complexity_label))
        self.wait()
        self.play(Write(method_label))
        self.wait(2)
        # # Final summary of the result




class FibonacciSummaryTable(Scene):
    def construct(self):
        # Create the title for the table
        title = Text("Fibonacci Methods: Time and Space Complexity", font_size=36)
        title.shift(2*UP)

        # Create the table data for the Fibonacci methods and complexities
        table_data = [
            ["Method", "Time Complexity", "Space Complexity"],
            ["Classical Recursive", "O(2^n)", "O(n)"],
            ["Dynamic Programming", "O(n)", "O(n) or O(1)"],
            ["Fast Matrix Exponentiation", "O(log(n))", "O(1)"],  # Corrected space complexity
            ["Binet's approximation", "O(1)", "O(1)"]  # Corrected space complexity

        ]
        
        # Create the table object
        summary_table = Table(
            [[cell for cell in row] for row in table_data],  # Use MathTex for each cell
            include_outer_lines=True,  # Draw outer lines
            h_buff=1,  # Horizontal padding between columns
            v_buff=0.5  # Vertical padding between rows
        )  # Scale to fit well in the scene

        # Position the table below the title
        summary_table.next_to(title, DOWN)

        # Display the title and table on screen
        self.play(Write(title))
        self.play(Create(summary_table))
        
        # Highlight each row (method) one by one
        for i in range(1, len(table_data)):
            self.play(summary_table.get_rows()[i].animate.set_fill(YELLOW, opacity=1))
            self.wait(3)
            self.play(summary_table.get_rows()[i].animate.set_fill(WHITE, opacity=1))

        # Hold the final table for a moment
        self.wait(3)



class FibonacciBinet(Scene):
    def construct(self):
        # Title
        title = Text("Fibonacci Computation with Binet's Formula", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.shift(2 * UP))
        
        # Explanation of Fibonacci Sequence
        fib_intro = Text("Fibonacci Sequence: 1, 1, 2, 3, 5, 8, 13, ...", font_size=24)
        self.play(Write(fib_intro))
        self.wait(2)
        
        # Binet's Formula
        binets_formula = MathTex(
            "F(n) = \\frac{\\phi^n - (1 - \\phi)^n}{\\sqrt{5}}",
            font_size=36,
            color=BLUE  # Change color to blue
        )
        binets_formula.next_to(fib_intro, DOWN)
        self.play(Write(binets_formula))
        self.wait(2)
        
        # Define phi
        phi_definition = MathTex(
            "\\phi = \\frac{1 + \\sqrt{5}}{2} \\approx 1.61803398875",
            font_size=24,
            color=BLUE  # Change color to blue
        )
        phi_definition.next_to(binets_formula, DOWN)
        self.play(Write(phi_definition))
        self.wait(2)
        
        # O(1) Complexity Explanation
        complexity = Text("Time and Space Complexity: O(1)", font_size=24)
        complexity.next_to(phi_definition, DOWN)
        self.play(Write(complexity))
        self.wait(2)
        
        # Not Exact Explanation
        not_exact = Text("Note: Result is not exact due to precision issues!", font_size=24, color=RED)
        not_exact.next_to(complexity, DOWN)
        self.play(Write(not_exact))
        self.wait(2)
        
        # Final Notes
        final_notes = Text("Binet's formula provides an approximation.", font_size=24)
        final_notes.next_to(not_exact, DOWN)
        self.play(Write(final_notes))
        self.wait(3)

        # End scene
        self.play(FadeOut(title), FadeOut(fib_intro), FadeOut(binets_formula),
                  FadeOut(phi_definition), FadeOut(complexity), FadeOut(not_exact), FadeOut(final_notes))










class FibonacciSquares(Scene):
    def construct(self):
        # Initial side lengths of the Fibonacci sequence (1, 1, 2, 3, 5, 8...)
        fibonacci_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
        colors = [BLUE, GREEN, YELLOW, ORANGE, PURPLE, RED, TEAL, MAROON]
        
        # Starting point for drawing
        position = ORIGIN
        squares = []
        
        # Directions for each step in the spiral: Right, Up, Left, Down
        directions = [RIGHT, UP, LEFT, DOWN]
        direction_index = 0
        
        # Draw each square in the Fibonacci sequence
        for i, size in enumerate(fibonacci_sequence):
            # Create a square with side length equal to the Fibonacci number
            square = Square(side_length=size, color=colors[i % len(colors)], fill_opacity=0.8)
            
            # Move position by half the current size + half of the next size in the current direction
            if i == 1:
                position += directions[direction_index] *1.5
            elif i > 1:
                position += directions[direction_index] * (size  + fibonacci_sequence[i - 1] )
            else:
                position += directions[direction_index] * size 
            print("i", i ,"position ", position,"size ", size,  " color ", colors[i % len(colors)])    
            square.move_to(position)
            squares.append(square)
            self.play(Create(square), run_time=1.5)
            self.wait()
            
            # Update the position for the next square
            # Change direction for the next square in the spiral
            direction_index = (direction_index + 1) % 4
            
        # Display all squares together
        self.wait(1)




class DescendingArrowWithText(Scene):
    def construct(self):
        # Create a red, vertical, descending arrow
        arrow = Arrow(
            start=UP*2,         # Starting point (higher)
            end=DOWN * 3,     # Ending point (lower by 2 units)
            color=RED,        # Set the color to red
            stroke_width=5    # Optional: make the arrow a bit thicker
        )

        # Create the mathematical label O(2^n) near the arrow's end
        label = MathTex(r"O(2^n)", color=RED)
        label.next_to(arrow.get_end(), DOWN)  # Position the label at the end of the arrow

        # Animate the creation of the arrow and the label
        self.play(Create(arrow), Write(label))
        self.wait(1)




class FunctionArrowWithImage(Scene):
    def construct(self):
        # Create a horizontal arrow representing the function "n -> F(n)"
        function_arrow = Arrow(
            start=LEFT * 3,               # Starting point to the left
            end=RIGHT * 3,                # Ending point to the right
            color=BLUE,                   # Color of the arrow
            buff=0,                       # No gap between start/end points and the arrow
            stroke_width=5                # Make the arrow a bit thicker
        )

        # Add a tick mark at the start to create the "maps to" look
        tick_mark = Line(
            function_arrow.get_start() + DOWN * 0.2,
            function_arrow.get_start() + UP * 0.2,
            color=BLUE
        )

        # Labels for "n" on the left and "F(n)" on the right
        n_label = MathTex("n", color=BLUE)
        fn_label = MathTex("F(n)", color=BLUE)

        n_label.next_to(function_arrow.get_start(), LEFT)   # Place "n" to the left of the arrow
        fn_label.next_to(function_arrow.get_end(), RIGHT)   # Place "F(n)" to the right of the arrow
        Qm = Text("?", color=BLUE, font_size = 60).next_to(function_arrow, DOWN)

        # Load and position the image at the top middle of the arrow
        image = ImageMobject("computerScreen.png").scale(0.5)  # Adjust scale as needed
        image.next_to(function_arrow.get_center(), UP, buff=0.5)  # Place the image above the arrow center

        # Add and animate all elements
        self.play(Write(n_label))
        self.play(Create(function_arrow), Create(tick_mark))
        self.play(Write(Qm))
        self.play(Write(fn_label))  # Display the labels "n" and "F(n)"
        self.play(FadeIn(image))
        self.wait(3)


if __name__ == "__main__":
    os.system("manim -pqk FiboClean.py FibonacciSquares")


































