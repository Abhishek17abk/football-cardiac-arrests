import streamlit as st
import streamlit.components.v1 as components

def app():
    st.title('Football’s popularity, cardiac safety awareness opportunity')
    st.write('Romanian club Inter Cristian’s 33-year-old Alexandru Vagner passed away on 30th September 2022 after suffering a heart attack during a training session at the clubs facility. His death is just the latest example of a footballing sudden death, but its a problem that is getting increased attention both on and off the pitch.')
    st.write ('The most renowned case occurred in the Euro 2020, when the Danish-playmaker Christian Eriksen was resuscitated after suffering an on-field cardiac arrest in a group stage match against Finland. He was given cardiopulmonary resuscitation and was later fitted with an implantable cardioverter-defibrillator, and returned to football eight months later, eventually playing for Manchester United. A dataset was compiled by fans and published on Kaggle with the help of various media reported sudden deaths in football. The analysis of this data provided some interesting insights.')
    html_temp = """<div class='tableauPlaceholder' id='viz1665694916541' style='position: relative'><noscript><a href='#'><img alt='Media Reported Heart Related Deaths By Decade ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FootballHeartRelatedDeaths&#47;HeartRelatedDeathsbyDecade&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='FootballHeartRelatedDeaths&#47;HeartRelatedDeathsbyDecade' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FootballHeartRelatedDeaths&#47;HeartRelatedDeathsbyDecade&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1665694916541');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, width=900,height=900)
    st.write('Most reported deaths (137 of 263) were attributed to heart-related conditions, and almost half of these heart-related sudden deaths (63 of 137) occurred in the last decade alone (2010-2019). In the current decade, the number of deaths reported has shown a further upward trend, with 25 deaths reported in just the last three years. The data is crude and might be inconclusive in terms of the coverage of all occurrences of deaths, but it does raise questions about whether the situation is improving or not. The problem of heart-related sudden deaths has also been the subject of study for many sports bodies and academic researchers. A 2020 study by Saarland University found that 76% of footballers under the age of 35 who encountered a sudden cardiac death had coronary heart disease.')
    st.write('Football associations have been trying to reduce heart-related incidents with initiatives such as the FA’s mandatory cardiac screening programme (1997), and pre-competition medical screening mandate (2006). The international football body’s Pre-Competition Medical Assessment comprises a physical examination, an ECG, and an echocardiography to check for heart-related abnormalities. According to a study published in the British Medical Journal (BMJ), this cross-disciplined medical examination is the best approach to check for heart-related irregularities in sports athletes. However, in a study published in the New England Journal of Medicine, in which FA’s 1997 screening programme was analysed, 75% of players who died of sudden cardiac arrest had no symptoms during screening. “In some cases, one cannot identify everyone at risk of sudden cardiac death, 80% of young individuals who die during exercise due to cardiac arrests never have symptoms, or a family history,” Dr Harshil Dhutia, consultant cardiologist, Glenfield Hospital, University hospitals of Leicester. Besides these undetectable heart abnormalities, events can happen on the football pitch, such as the football hitting the chest or physical contact with a player that can contribute to sudden cardiac arrest. ')
    
    st.write('Some causes of sudden cardiac arrest are not necessarily inherited and can be acquired after people have been screened. For instance, in January, the player’s report would have looked normal, but he might have acquired a heart disease in March. Viral infections affecting the heart muscle, which received a lot of attention during the pandemic, is one of the best examples of acquired heart conditions that can lead to sudden cardiac arrest. “Its really important that people are aware of symptoms and family history from screening, but they also need to be made aware of the limitations of screening.  Thus, one cannott emphasise enough the importance of automated external defibrillators (AED) and cardiopulmonary resuscitation (CPR) training,” says Dhutia. The Saarland University study shared one key statistic: CPR resulted in a survival rate of 85% with the use of an AED, compared to 35% without. The government’s sport ministry (DCMS) now obliges its community sport body Sport England to only award grant money to venues that provide AED. A press release from The Digital, Culture, Media and Sport department said, “At the grassroots sport level, all capital funding awards for sports venues made by Sport England must include AED provision if it is not already available”. Sport England along with the FA have set up a fund to provide 2,000 AEDs to grassroots football clubs and according to a recent FOI request, 1,538 applications from local clubs have been received till April.')
    st.write('A study funded by the FA which Dhutia co-authored shared that most clubs in all divisions of the English Football League have satisfactory medical provisions, including the availability of AEDs on match day. However, the study identified a gap in the cardiovascular safety of footballers in the lower divisions.  In contrast to the Premiership where all clubs provided AED training to designated staff, almost 30 percent of clubs in the lower divisions had available devices but no training for the staff.  “Necessarily, there’s no problem at the highest level of sport. The issue lies whether there is equitable care and availability and training at lower levels of sport, particularly grassroots, recreational and school sport. It’s nowhere near the level of the highest level of sport,” says Dhutia. He adds, “Its really important for those who do have AEDs to understand that its not just about having an AED, it is about getting regular training, making sure staff are updated. For example, in hospitals, doctors and hospital nurses and healthcare professionals have a requirement for periodic training, even though they perform these procedures such as resuscitation frequently.')
    st.write('This Saarland University study also highlighted the need for staff CPR training along with immediate access to AEDs as a key to maximise the survival rates. Dhutia debunked the misconception among people that such conditions affect only athletes. “These are genetic conditions, so they do not have a unique prediction for competitive sport, people think it only happens to athletes due to the media coverage, whereas it can impact anyone.” As the majority of deaths occur among the general population,it may not get the same media attention as athletes, Dhutia feels, “We are probably looking at an under-representation, yet the actual number of deaths are likely to be higher. A study published in  The European Resuscitation Council’s journal, Resuscitation, explains how the football media can be used as a platform to raise awareness on sudden cardiac arrests. “The surge of public emotion in response to the sudden heart attack of Christian Eriksen can be used as an example to support the logic of CPR education.” FIFA’s estimate of 443 million football fans suggest that there is a huge audience where awareness can be raised. The vast popularity of the sport can become a driving force to raise awareness on strategies to prevent deaths from sudden cardiac arrests.')


