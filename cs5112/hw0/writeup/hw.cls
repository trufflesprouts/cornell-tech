\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{hw_template}

\LoadClass[12pt]{article}
\RequirePackage[utf8]{inputenc}
\RequirePackage[margin=1in]{geometry}

\RequirePackage{libertine}
\RequirePackage{parskip}

\RequirePackage{amsthm,amsmath,amssymb,hyperref}
\RequirePackage{tikz}
\usetikzlibrary{arrows,automata}

\RequirePackage{pgfplots}
\pgfplotsset{compat=1.16}

\pagestyle{plain}
\thispagestyle{empty}

\definecolor{carnellian}{RGB}{190,20,20}

\usepackage{dirtree}
\usepackage{nimbusmononarrow}

\newcommand{\N}{\mathbb{N}}
\newcommand{\bigO}{\mathcal{O}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Problems:

\theoremstyle{definition}
\newtheorem{problem}{Problem}

\newcounter{subq}[problem]
\newenvironment{subproblem}
{\refstepcounter{subq} \begin{itemize} \item[(\alph{subq})]}
{\end{itemize} \medskip}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Solutions:

\RequirePackage{ifthen}
\RequirePackage{environ}

\newboolean{withsolutions}
\setboolean{withsolutions}{false}

\NewEnviron{solution}[1][80pt]{
    \ifthenelse{\boolean{withsolutions}}
    {\vspace{10pt} \textcolor{blue}{\BODY} \vspace{10pt}}
    {\vspace{20pt}}
}

\newboolean{withhints}
\setboolean{withhints}{false}

\NewEnviron{hints}[1][80pt]{
    \ifthenelse{\boolean{withhints}}
    {\vspace{10pt} \textcolor{red}{Hints: \begin{itemize}\BODY\end{itemize}} \vspace{10pt}}
    {\vspace{20pt}}
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Front Matter:
\setlength\fboxrule{.5mm}\setlength{\fboxsep}{1.2mm}
\newlength\courseheader
\setlength\courseheader\textwidth
\addtolength\courseheader{-4mm}

\AtBeginDocument{
    \fbox{
        \parbox{\courseheader}{
        Algorithms for Applications\hfill HW\hwnum: {\it \title}  \\
        CS 5112 Fall 2025 \hfill \textbf{Due: \duedate}
        }
    }
    \vspace{5pt}



    % \noindent
    
    % \begin{tabular*}{\textwidth}{l @{\extracolsep{\fill}} r}
    %     \textbf{CS 2800 - Discrete Structures} 
    %         & \textbf{Fall 2022} \\
    %     \textbf{HW\hwnum: \title} &  \textbf{Due: \duedate}
    % \end{tabular*}\\
    % \rule[2ex]{\textwidth}{2pt}

    \ifthenelse{\boolean{withsolutions}}{}{
    \textbf{Homework Instructions:} The homework contains mainly three types of tasks:
    \begin{itemize}

      \item \textbf{Coding.} You can find a template for all the coding problems
        inside the \texttt{problems.zip} in the module. Please use these
        templates, to ensure the files and functions have the same names that
        the autograder will check for.
        
        Inside the \texttt{problems} directory, you will find the \texttt{tests}
        directory, which contains some sample test cases for the different
        problems. These test cases are intended to help you test and debug your
        solution. However, note that Gradescope will run a more comprehensive
        test suite. Feel free to add additional test cases to further test your
        code. 

        In order to run the tests for a particular problem $n$, navegate into \texttt{problems/tests} and run: 
        \texttt{python3 test\_problem\_n.py}

        \item \textbf{Algorithm Description.} When a questions requires
          designing an algorithm, you should describe what your algorithm does
          in the writeup, in clear concise prose.
          You can cite algorithms covered in class to help your description. You
          should also argue for your algorithm's asymptotic run time or, in some
          cases when indicated in the problem, 
          for the run time bounds of your implementation.


        \item \textbf{Empirical Performance Analysis.} Some questions may ask
          you to do an empirical performance analysis of one or more algorithms' runtime
          under different values of $n$. For these questions, you should
          generate at least ten test cases for the implementation, for various
          values of $n$ (include both small and large instances).  
          Then, measure the performance locally on your own
          system, by taking the
          median runtime of the implementation over ten or more iterations.
          Graph the resulting median run times. The x-axis should be instance
          size and the y-axis should be median run time. You can use any
          plotting library of your choice. If you have never plotted on Python
          before,
          \href{https://matplotlib.org/stable/tutorials/introductory/pyplot.html}{this
          matplotlib turorial} has some examples.  
              
        If several subquestions in a problem ask you to provide performance
        analysis, please do them all in the same environment (same system and
        configuration), in order to have a more accurrate comparison between
        algorithms. You can include graphs for a same problem in the same plot,
        as long as the different graphs are properly labeled.

        For these types of questions, you will not need to submit the tests you
        generate or your code for benchmarking or plotting the algorithms.
        However, you should include the graphs you generate into the write-up.
        You should also write about what you observe from the analysis and
        potentially compare it to the complexity analysis.  Finally, also
        include a description of the environment (CPU, operating system and
        version, amount of memory) you did the testing on.
    \end{itemize} 

    \textbf{Submission Instructions:} 
    Hand in your solutions electronically on Gradescope. There are two active
    assignments for this problem set on Gradescope: one with the autograder,
    where you submit your code, and another one where you submit the write-up.

    \textbf{Coding Submission:}
    You only need to submit the code for the specific functions we ask you to implement. While you will write additional code
    to generate the performance analysis graphs when required, you do not need to submit that code.

    To submit to the autograder, please zip the \texttt{problems} directory we provided you with. Therefore, your zipped file should have the following structure:

    \dirtree{%
    .1 problems.
    .2 problem\_1.
    .3 p1\_a.py.
    .3 p1\_b.py.
    .3 \dots .
    .2 problem\_2.
    .3 p2.py.
    .2 \dots .
    }
    
    In order to ensure your code runs correctly, do not change the names of the
    files or functions we have provide you. Additionally, do not import external
    python libraries in these files, you don't need any libraries to solve the
    coding assignments. Finally, if you write any helper functions for your
    solutions, please include them in the same files as the functions that call
    them.
    
    We have some public tests in the autograder to verify that all the required
    files are included, so you will be able to verify on Gradescope that your
    work is properly formatted shortly after submitting. We strongly encourage
    checking well ahead of the due date that your solutions work on the
    autograder, and seeking out assistance from the TAs should it not. We cannot
    guarantee being responsive the night the assignment is due. 
    %{\color{red} (Carolina: Should say something about plan submitting ahead to ahve time to fix any error and/or feel free to reach out to the TAs for help? Also, need to double-check how the autograder looks like from a student's perspective)}

    %{\color{red} (Carolina: Do we want to provide any additional resources? The old template had ``[a] guide to programming assignments...for details and tips'' but I don't know what that means).}
    
    \textbf{Write-up Submission:}
    Your write-up should be a nicely formatted PDF prepared using the
    \LaTeX \ template on
    \href{https://canvas.cornell.edu/courses/56135/modules}{Canvas}, where you can type in your answer in the \texttt{main.tex} file. If you do not have previous experience using 
    \LaTeX, we recommend using \href{https://www.overleaf.com/}{Overleaf}. It
    is an online \LaTeX \ editor, where you can upload and edit the template we
    provide. For additional advice on typesetting your work, please refer to
    the \textit{resources} directory on the course's
    \href{https://github.com/tomrist/cs5112-fall2023}{website}. 
   
    % \textbf{Design-an-Algorithm Instructions:}
    % Homework problems often ask you to design an algorithm. In this case,  you must:
    % \begin{enumerate}
    %     \item
    %     explain your algorithm at a high level {\it in English}. You can use pseudocode (but not code) as needed to make your ideas clearer, but remember to keep all explanations at a high level,
    %     \item 
    %     prove the algorithm's correctness, and 
    %     \item
    %     analyze its running time, that is, you must show the running time is bounded by a polynomial function of the input size. 
    % \end{enumerate}
    % You may sometimes realize that you can solve a homework problem using an  algorithm from lecture or the text book as a black box. We call this a \emph{reduction}. In this case, you need not     explain the details of the existing algorithm, its running time and correctness. However, you  must fully explain the reduction by  providing
    % \begin{enumerate}
    % \item
    % a clear reference to the existing algorithm, along with the protocol that turns an instance of the homework problem into an input for this algorithm,  
    % \item  a proof that the output given by the existing algorithm on the input created by your protocol correctly solves the homework problem, and
    % \item
    % a running time analysis that bounds the time of the combined process of creating the input for the existing algorithm, and executing the algorithm on this input by a polynomial function of the homework problem's input size.
    % \end{enumerate}
    

    \textbf{Academic Integrity:} You may use online sources or tools (such as code
    generation tools), but any tools you use should be explicitly acknowledged
    and you must explain how you used them. You are responsible for the
    correctness of submitted solutions, and we expect you to understand them and
    be able to explain them when asked by teaching staff. 
    
    \textbf{Collaboration Policy:} Collaboration (in groups of up to three students) is encouraged while solving the problems, but: 
    \begin{enumerate}
        \item
        list the netids of those in your group;
        \item
        you may discuss ideas and approaches, but you should not write a detailed argument or code outline together;
        \item
        notes of your discussions should be limited to drawings and a few keywords;
        you must {\bf write up the solutions and write code on your own}.
\end{enumerate}



    
%    \noindent\makebox[\linewidth]{\rule{\textwidth}{0.4pt}}
}
    
%    \vspace{20pt}
}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Challenge:
\newcommand{\challenge}{
    \ifthenelse{\boolean{withsolutions}}{}{
    
    \newpage

        \fbox{
        \parbox{\courseheader}{
        Algorithms for Applications\hfill HW\hwnum: Challenge Problem  \\
        CS 5112 Fall 2025 \hfill \textbf{Due: \duedate}
        }
    }
    \vspace{5pt}

    % {\color{red} Carolina: Do we want to have challenge problems? And how will they impact students grades?}

    {\bf Instructions:} Challenge problems are, as the term indicates, {\it challenging}. They do not count for the homework score (90\% of your course grade); instead, they are considered separately as extra credit over your course grade (additional 15\% in total, 3.75\% per assignment). 
    
    % when computing your course grade (and weighted at 2.5\% for CS4820, and at 7.5\% for CS5820). In addition, they will be taken into account when determining whether you deserve an \textsf{A}$^+$.
    
    Questions about challenge problems will have lowest priority in office hours, and we do not provide assistance beyond a few hints to help you know whether you are on the right track.
    
    \textbf{Submission Instructions:} You can choose not to hand a submission, but we encourage everyone to attempt the challenge problem. If you solve it, please hand in your answers (both, the coding and the write-up) through Gradescope, along with the rest of your assignment.
    
    % If you manage to solve it (or make good progress), please hand in the answer for this question on gradescope as a separate document and submit it for the ``HW~\hwnum~Challenge'' on gradescope. 
    % Any answers to the challenge problem included in your main HW\hwnum submission will be ignored. Do not submit anything to ``HW~\hwnum~Challenge'' if you do not attempt the challenge problem.
    
    \textbf{Academic Integrity and Collaboration Policy:} The same guidelines apply to challenge problems as for the regular homework problems.
    
    \noindent\makebox[\linewidth]{\rule{\textwidth}{0.4pt}}
    \vspace{10pt}}

    
}
