import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String user_reply = "";
        String convo = "True";
        String line;
        boolean firstTime = true;
        do{
            try{
                if(!firstTime){
                    System.out.print("User: ");
                    user_reply = sc.nextLine();
                }
                else{
                    firstTime = false;
                }

                ProcessBuilder pb = new ProcessBuilder("python","handy_chatbot.py"," "+user_reply);
                Process p = pb.start();
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                user_reply = in.readLine();
//                System.out.println(user_reply);
                for(int i=0;i<3;i++){
                    in.readLine();
                }

                convo = in.readLine();
//                System.out.println("convo = "+convo);
                while ((line = in.readLine()) != null) {
                    System.out.println(line);
                }

            }catch(Exception e){System.out.print(e);}


        }while(convo.equals("True"));

//        do {
//            user_reply = sc.nextLine();
//            Process p = Runtime.getRuntime().exec("python handy_chatbot.py "+user_reply);
//            BufferedReader br = new BufferedReader(new InputStreamReader(p.getInputStream()));
//            System.out.println(br.readLine());\
//            try (BufferedReader br = new BufferedReader(new FileReader("bot_replies/" + state + ".txt"))) {
//                String line;
//                while ((line = br.readLine()) != null) {
//                    System.out.println(line);
//                }
//            } catch (IOException e) {
//                throw new RuntimeException(e);
//            }
////            System.out.println(bot_reply);
//
//        } while ((String) state.__tojava__(String.class) != end_state);



//        PythonInterpreter pi = new PythonInterpreter();
//        Scanner sc = new Scanner(System.in);
//
//        pi.execfile("handy_chatbot.py");
//        String end_state = "end_convo";
//        PyObject state = null;
//        PyObject bot_reply = null;
//        String user_reply = "";
//        System.out.println();
//        try (BufferedReader br = new BufferedReader(new FileReader("bot_replies/start_convo.txt"))) {
//            String line;
//            while ((line = br.readLine()) != null) {
//                System.out.println(line);
//            }
//        } catch (IOException e) {
//            throw new RuntimeException(e);
//        }
//        do {
//            user_reply = sc.nextLine();
//            state = pi.eval("bot_reply(" + user_reply + ")");
//            try (BufferedReader br = new BufferedReader(new FileReader("bot_replies/" + state + ".txt"))) {
//                String line;
//                while ((line = br.readLine()) != null) {
//                    System.out.println(line);
//                }
//            } catch (IOException e) {
//                throw new RuntimeException(e);
//            }
////            System.out.println(bot_reply);
//
//        } while ((String) state.__tojava__(String.class) != end_state);


    }
}