#------------------------------------------------------------------------------------------------------------------
#   Ejemplo de base de conocimiento para diagnóstico
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------

from utils import *
from logic import *

#------------------------------------------------------------------------------------------------------------------
#   Conocimiento general
#------------------------------------------------------------------------------------------------------------------

clauses=[]

# Enfermedades

        # Padecimientos de JP
clauses.append(expr("Fiebre(x) & DolorGarganta(x) & Bronquitis(x) & Neumonia(x) & Conjuntivitis(x)==> Enfermo(x, InfeccionAdenovirus)"))
clauses.append(expr("DiarreaSangre(x) & DolorAbdominal(x) & Fiebre(x) & DolorCabeza(x) & Nauseas(x) ==> Enfermo(x, Campilobacteriosis)"))
clauses.append(expr("DiarreaSangre(x) & DolorAbdominal(x) & Fiebre(x) & DolorCabeza(x) & Vomito(x) ==> Enfermo(x, Campilobacteriosis)"))
clauses.append(expr("DiarreaAcuosa(x) & DolorAbdominal(x) & FrecuenciaCardiacaAlta(x) & Deshidratacion(x) & Fiebre(x) & Nauseas(x) & GainGlobulosBlancos(x) & InsuficienciaRenal(x) & NoHambre(x) & InflamacionAbdominal(x) & PerdidaDePeso(x) & SangreFecal(x) & PusFecal(x) ==> Enfermo(x, ClostridiumDifficile)"))
clauses.append(expr("DiarreaAcuosa(x) & Vomito(x) & Fiebre(x) & DolorAbdominal(x) & Cansancio(x) & Irritacion(x) & Deshidratacion(x) ==> Enfermo(x, Rotavirus)"))
clauses.append(expr("Diarrea(x) & Colicos(x) & Fiebre(x) & Nauseas(x) & Vomitos(x) & Escalofrios(x) & DolorCabeza(x) & SangreFecal(x) ==> Enfermo(x, Salmonelosis)"))
        # Padecimientos de Juan Pablo
clauses.append(expr("DolorAbdominal(x) & InflamacionAbdominal(x) & Eructos(x) & Nauseas(x) ==> Enfermo(x, Dispepsia)"))
clauses.append(expr("SensAbdomen(x) & Gases(x) & Fiebre(x) & Escalofrios(x) & Nauseas(x) & Vomito(x) & NoHambre(x) ==> Enfermo(x, Diverticulitis)"))
clauses.append(expr("SangreFecal(x) ==> Enfermo(x, CancerEstomago)"))
clauses.append(expr("SangreFecal(x) ==> Enfermo(x, CancerIntestinoDelgado)"))
clauses.append(expr("SangreFecal(x) ==> Enfermo(x, Campilobacteriosis)"))
clauses.append(expr("Diarrea(x) ==> Enfermo(x, EnfermedadCeliaca)"))
clauses.append(expr("Diarrea(x) ==> Enfermo(x, SindromeIntestinoIrritable)"))
clauses.append(expr("Diarrea(x) ==> Enfermo(x, ColitisUlcerosa)"))
clauses.append(expr("Diarrea(x) ==> Enfermo(x, EnfermedadCrohn)"))
clauses.append(expr("Diarrea(x) ==> Enfermo(x, Campilobacteriosis)"))
clauses.append(expr("Diarrea(x) ==> Enfermo(x, ClostridiumDifficile)"))
clauses.append(expr("Diarrea(x) ==> Enfermo(x, EscherichiaColi)"))
clauses.append(expr("Diarrea(x) ==> Enfermo(x, Rotavirus)"))
clauses.append(expr("Diarrea(x) ==> Enfermo(x, Salmonelosis)"))
clauses.append(expr("DolorTragar(x) & DificultadTragar(x) & PerdidaDePeso(x) & DolorEsternon(x) & Ronquera(x) & Tos(x) & Indigestion(x) & Acidez(x) & MasaPiel(x) ==> Enfermo(x, CancerEsofago)"))
clauses.append(expr("Estreñimiento(x) ==> Enfermo(x, EnfermedadCeliaca)"))
clauses.append(expr("Estreñimiento(x) ==> Enfermo(x, Diverticulosis)"))

        # Padecimientos de Francelio
clauses.append(expr("SensacionDolorosa(x) & SensacionArdiente(x) & Regurgitacion(x) & DolorPecho(x) & Nauseas(x) & DificultadTragar(x) & TosCronica(x) ==> Enfermo(x, ReflujoGastroesofasico)"))
clauses.append(expr("SensacionDolorosa(x) & SensacionArdiente(x) & Regurgitacion(x) & DolorPecho(x) & Nauseas(x) & DolorTragar(x) & Ronquera(x) ==> Enfermo(x, ReflujoGastroesofasico)"))
clauses.append(expr("SensacionDolorosa(x) & SensacionArdiente(x) & Regurgitacion(x) & DolorPecho(x) & Nauseas(x) & DificultadTragar(x) & Ronquera(x) ==> Enfermo(x, ReflujoGastroesofasico)"))
clauses.append(expr("SensacionDolorosa(x) & SensacionArdiente(x) & Regurgitacion(x) & DolorPecho(x) & Nauseas(x) & DolorTragar(x) & TosCronica(x) ==> Enfermo(x, ReflujoGastroesofasico)"))
clauses.append(expr("DistensionAbdominal(x) & Diarrea(x) & Estreñimiento(X) & Gases(X) & IntoleranteLactosa(x) & HecesBlandas(x) & HecesGrasosas(x) & HecesVoluminosas(x) & HecesMalOlor(x) & Nauseas(x) & DolorAbdominal(x) ==> Enfermo(x, EnfermedadCeliaca)"))
clauses.append(expr("DistensionAbdominal(x) & Diarrea(x) & Estreñimiento(X) & Gases(X) & IntoleranteLactosa(x) & HecesBlandas(x) & HecesGrasosas(x) & HecesVoluminosas(x) & HecesMalOlor(x) & Vomito(x) & DolorAbdominal(x) ==> Enfermo(x, EnfermedadCeliaca)"))
clauses.append(expr("Dolor(x) & CambiosAspecto(x) & CambiosFrecuencia(x) & SensacionIncompleta(x) & GainGases(x) & PerdidaDePeso(x) & DiarreaNocturna(x) & Vomito(x) & DolorGases(x) ==> Enfermo(x, SindromeIntestinoIrritable)"))
clauses.append(expr("Dolor(x) & CambiosAspecto(x) & CambiosFrecuencia(x) & SensacionIncompleta(x) & MucosidadHeces(x) & PerdidaDePeso(x) & DiarreaNocturna(x) & Vomito(x) & DolorEvacuacion(x) ==> Enfermo(x, SindromeIntestinoIrritable)"))
clauses.append(expr("Calambre(x) & CambiosAspecto(x) & CambiosFrecuencia(x) & SensacionIncompleta(x) & GainGases(x) & PerdidaDePeso(x) & DiarreaNocturna(x) & Vomito(x) & DolorGases(x) ==> Enfermo(x, SindromeIntestinoIrritable)"))
clauses.append(expr("Calambre(x) & CambiosAspecto(x) & CambiosFrecuencia(x) & SensacionIncompleta(x) & MucosidadHeces(x) & PerdidaDePeso(x) & DiarreaNocturna(x) & Vomito(x) & DolorEvacuacion(x) ==> Enfermo(x, SindromeIntestinoIrritable)"))
clauses.append(expr("InflamacionAbdominal(x) & CambiosAspecto(x) & CambiosFrecuencia(x) & SensacionIncompleta(x) & GainGases(x) & PerdidaDePeso(x) & DiarreaNocturna(x) & Vomito(x) & DolorGases(x) ==> Enfermo(x, SindromeIntestinoIrritable)"))
clauses.append(expr("InflamacionAbdominal(x) & CambiosAspecto(x) & CambiosFrecuencia(x) & SensacionIncompleta(x) & MucosidadHeces(x) & PerdidaDePeso(x) & DiarreaNocturna(x) & Vomito(x) & DolorEvacuacion(x) ==> Enfermo(x, SindromeIntestinoIrritable)"))
clauses.append(expr("Dolor(x) & Nauseas(x) & SensacionLlenura(x) & NoHambre(x) & PerdidaDePeso(x) ==> Enfermo(x, Gastritis)"))
clauses.append(expr("Dolor(x) & Vomito(x) & SensacionLlenura(x) & NoHambre(x) & PerdidaDePeso(x) ==> Enfermo(x, Gastritis)"))
clauses.append(expr("MolestiaAbdomen(x) & Nauseas(x) & SensacionLlenura(x) & NoHambre(x) & PerdidaDePeso(x) ==> Enfermo(x, Gastritis)"))
clauses.append(expr("MolestiaAbdomen(x) & Vomito(x) & SensacionLlenura(x) & NoHambre(x) & PerdidaDePeso(x) ==> Enfermo(x, Gastritis)"))
clauses.append(expr("Nauseas(x) & Vomito(x) ==> Enfermo(x, Gastroenteritis)"))
clauses.append(expr("Dolor(x) & Calambres(x) & Estreñimiento(x) & DistencionAbdominal(x) & NoHambre(x) ==> Enfermo(x, Diverticulosis)"))
clauses.append(expr("Dolor(x) & Calambres(x) & Estreñimiento(x) & Gas(x) & NoHambre(x) ==> Enfermo(x, Diverticulosis)"))

        # Padecimientos de Michel
clauses.append(expr("DiarreaSangre(x) & AltaNecesidadDefecar(x) & PerdidaDeVascularidad(x) & Anemia(x) ==> Enfermo(x, ColitisUlcerosa)"))
clauses.append(expr("HecesClaras(x) & OrinaOscura(x) & Ictericia(x) & EnzimasHepaticas(x) & DolorAbdominal(x) ==> Enfermo(x, Hepatitis)"))
clauses.append(expr("Diarrea(x) & Colicos(x) & DolorAbdominal(x) & Anemia(x) ==> Enfermo(x, EnfermedadCrohn)"))
clauses.append(expr("DolorAbdominal(x) & Nauseas(x) & NoHambre(x) & Acidez(x) ==> Enfermo(x, UlcerasPepticas)"))
clauses.append(expr("PerdidaDePeso(x) & Fatiga(x) & Ictericia(x) & HinchazonAbdomen(x) & DolorAbdominal(x) ==> Enfermo(x, CirrosisHepatica)"))
clauses.append(expr("InflamacionPeritonea(x) & MalAliento(x) & SangreFecal(x) & Hipersensibilidad(x) ==> Enfermo(x, InfartoIntestinal)"))

# Tratamientos para enfermedades

        # Tratamientos de JP
clauses.append(expr("Enfermo(x, InfeccionAdenovirus) ==> Tratamiento(Sintomatico, x)"))
clauses.append(expr("Enfermo(x, Campilobacteriosis) ==> Tratamiento(Sintomatico, x)"))
clauses.append(expr("Enfermo(x, Campilobacteriosis) ==>  Tratamiento(Eritromicina, x)"))
clauses.append(expr("Enfermo(x, Campilobacteriosis) ==> Tratamiento(Sintomatico, x) "))
clauses.append(expr("Enfermo(x, Campilobacteriosis) ==> Tratamiento(Azitromicina, x)"))
clauses.append(expr("Enfermo(x, ClostridiumDifficile) ==> Tratamiento(Sintomatico, x)"))
clauses.append(expr("Enfermo(x, ClostridiumDifficile) ==> Tratamiento(Metronidazol, x)"))
clauses.append(expr("Enfermo(x, ClostridiumDifficile) ==> Tratamiento(Vancomicina, x)"))
clauses.append(expr("Enfermo(x, Ecoli) ==> Tratamiento(Sintomatico, x)"))
clauses.append(expr("Enfermo(x, Rotavirus) ==> Tratamiento(Sintomatico, x)"))
clauses.append(expr("Enfermo(x, Rotavirus) ==> Tratamiento(Fluoroquinolonas, x)"))
clauses.append(expr("Deshidratacion(x) ==> Tratamiento(TomarAgua, x)"))
clauses.append(expr("Deshidratacion(x) ==> Tratamiento(TomarSuero, x)"))
clauses.append(expr("Fiebre(x) ==> Tratamiento(Antipireticos, x)"))
clauses.append(expr("Diarrea(x) & Vomito(x) ==> Tratamiento(DietaAstringente, x)"))
clauses.append(expr("Diarrea(x) & Vomito(x) ==> Tratamiento(TomarSuero,x)"))
clauses.append(expr("DiarreaAcuosa(x) & Vomito(x) ==> Tratamiento(DietaAstringente, x)"))
clauses.append(expr("DiarreaAcuosa(x) & Vomito(x) ==> Tratamiento(TomarSuero,x)"))
clauses.append(expr("DolorGarganta(x) ==> Tratamiento(Analgesico, x)"))
clauses.append(expr("DolorCabeza(x) ==> Tratamiento(Analgesico, x)"))
clauses.append(expr("DolorAbdominal(x) ==> Tratamiento(Analgesico, x)"))
clauses.append(expr("CalambreAbdominal(x) ==> Tratamiento(Analgesico, x)"))
clauses.append(expr("SensAbdominal(x) ==> Tratamiento(Analgesico, x)"))
clauses.append(expr("Colicos(x) ==> Tratamiento(Analgesico, x)"))
clauses.append(expr("Dolor(x) ==> Tratamiento(Analgesico, x)"))

        # Tratamientos de Juan Pablo
clauses.append(expr("Enfermo(x,Dispepsia) ==> Tratamiento(TomarBloqH2,x)"))
clauses.append(expr("Enfermo(x,Dispepsia) ==> Tratamiento(TomarSimeticona,x)"))
clauses.append(expr("Enfermo(x,Dispepsia) ==> Tratamiento(TomarAntibioticos,x)"))
clauses.append(expr("Enfermo(x,Dispepsia) ==> Tratamiento(TomarAntiDepresivos,x)"))
clauses.append(expr("Enfermo(x,Dispepsia) ==> Tratamiento(TomarProcineticos,x)"))
clauses.append(expr("Enfermo(x,Dispepsia) ==> Tratamiento(TomarAntiemeticos,x)"))
clauses.append(expr("Enfermo(x,Diverticulitis) ==> Tratamiento(Reposo,x)"))
clauses.append(expr("Enfermo(x,Diverticulitis) ==> Tratamiento(Dieta,x)"))
clauses.append(expr("Enfermo(x,Diverticulitis) ==> Tratamiento(HidraVenosa,x)"))
clauses.append(expr("Enfermo(x,Diverticulitis) ==> Tratamiento(Analgesicos,x)"))
clauses.append(expr("Enfermo(x,Diverticulitis) ==> Tratamiento(TomarAntibioticos,x)"))
clauses.append(expr("SangreFecal(x) ==> Tratamiento(TomarSuplementosDeFibra,x)"))
clauses.append(expr("SangreFecal(x) ==> Tratamiento(TomarAblandadores,x)"))
clauses.append(expr("SangreFecal(x) ==> Tratamiento(BañoTibio,x)"))
clauses.append(expr("SangreFecal(x) ==> Tratamiento(Crema,x)"))
clauses.append(expr("Diarrea(x) ==> Tratamiento(TomarPeptoBismol,x)"))
clauses.append(expr("Enfermo(x,CancerEsofago) ==> Tratamiento(QuimioTerapia,x)"))
clauses.append(expr("Enfermo(x,CancerEsofago) ==> Tratamiento(RadioTerapia,x)"))
clauses.append(expr("Enfermo(x,CancerEsofago) ==> Tratamiento(TomarTrastuzumab,x)"))
clauses.append(expr("Estreñimiento(x) ==> Tratamiento(TomarSuplementosDeFibra,x)"))
clauses.append(expr("Estreñimiento(x) ==> Tratamiento(TomarAgua,x)"))
clauses.append(expr("Estreñimiento(x) ==> Tratamiento(TomarAblandadores,x)"))

        # Tratamientos de Francelio
clauses.append(expr("Enfermo(x,ReflujoGastroesofasico) ==> Tratamiento(TomarAntiacidos,x)"))
clauses.append(expr("Enfermo(x,ReflujoGastroesofasico) ==> Tratamiento(TomarBloqueadorHistamina,x)"))
clauses.append(expr("Enfermo(x,ReflujoGastroesofasico) ==> Tratamiento(TomarInhibidoresBombaProtones,x)"))
clauses.append(expr("Enfermo(x,EnfermedadCeliaca) ==> Tratamiento(TomarVitaminas,x)"))
clauses.append(expr("Enfermo(x,EnfermedadCeliaca) ==> Tratamiento(TomarSuplementoDietetico,x)"))
clauses.append(expr("Enfermo(x,SindromeIntestinoIrritable) ==> Tratamiento(Sintomatico,x)"))
clauses.append(expr("Enfermo(x,Gastritis) ==> Tratamiento(TomarAntihistaminicos,x)"))
clauses.append(expr("Enfermo(x,Gastritis) ==> Tratamiento(TomarAntiacidos,x)"))
clauses.append(expr("Enfermo(x,Gastritis) ==> Tratamiento(TomarAntihistaminicos,x)"))
clauses.append(expr("Enfermo(x,Gastritis) ==> Tratamiento(TomarInhibidoresBombaProtones,x)"))
clauses.append(expr("Enfermo(x,Gastroenteritis) ==> Tratamiento(TomarSuero,x)"))
clauses.append(expr("Enfermo(x,Gastroenteritis) ==> Tratamiento(TomarElectrolitos,x)"))
clauses.append(expr("Enfermo(x,Gastroenteritis) ==> Tratamiento(Sintomatico,x)"))
clauses.append(expr("Enfermo(x,Diverticulosis) ==> Tratamiento(TomarAntibioticos,x)"))
clauses.append(expr("Enfermo(x,Diverticulosis) ==> Tratamiento(DietaLiquidos,x)"))
clauses.append(expr("Enfermo(x,Diverticulosis) ==> Tratamiento(TomarAntiespasmodicos,x)"))
clauses.append(expr("Enfermo(x,Diverticulosis) ==> Tratamiento(TomarAcetaminofeno,x)"))
clauses.append(expr("Enfermo(x,Diverticulosis) ==> Tratamiento(Sintomatico,x)"))

        # Tratamientos de Michel
clauses.append(expr("Enfermo(x,ColitisUlcerosa) ==> Tratamiento(TomarAntiinflamatorios,x)"))
clauses.append(expr("Enfermo(x,ColitisUlcerosa) ==> Tratamiento(SupresoresInmunitarios,x)"))
clauses.append(expr("Enfermo(x,ColitisUlcerosa) ==> Tratamiento(TomarAntidiarreicos,x)"))
clauses.append(expr("Enfermo(x,Hepatitis) ==> Tratamiento(Cirugia,x)"))
clauses.append(expr("Enfermo(x,Hepatitis) ==> Tratamiento(TrasplanteHigado,x)"))
clauses.append(expr("Enfermo(x,EnfermedadCrohn) ==> Tratamiento(Loperamida,x)"))
clauses.append(expr("Enfermo(x,EnfermedadCrohn) ==> Tratamiento(TomarAntiespasmodicos,x)"))
clauses.append(expr("Enfermo(x,EnfermedadCrohn) ==> Tratamiento(TomarAcidoAminosalicilico,x)"))
clauses.append(expr("Enfermo(x,UlcerasPepticas) ==> Tratamiento(TomarInhibidoresBombaProtones,x)"))
clauses.append(expr("Enfermo(x,CirrosisHepatica) ==> Tratamiento(TrasplanteHepatico,x)"))
clauses.append(expr("Enfermo(x,InfartoIntestinal) ==> Tratamiento(MedicamentosAnticoagulantes,x)"))
clauses.append(expr("Enfermo(x,InfartoIntestinal) ==> Tratamiento(Enterostomia,x)"))

# Base de conocimiento
Med_kb = FolKB(clauses)

#------------------------------------------------------------------------------------------------------------------
#   Conocimiento sobre un paciente
#------------------------------------------------------------------------------------------------------------------

print(" █▄▄ █ █▀▀ █▄░█ █░█ █▀▀ █▄░█ █ █▀▄ █▀█  ▄▀█ █░░")
print(" █▄█ █ ██▄ █░▀█ ▀▄▀ ██▄ █░▀█ █ █▄▀ █▄█  █▀█ █▄▄")
print(" ░░░ ░ ░░░ ░░░░░░░░ ░░░ ░░░░ ░ ░░░ ░░░  ░░░ ░░░")
print(" █▀▀ █░█ ▄▀█ ▀█▀  █▀▄▀█ █▀▀ █▀▄ █ █▀▀ █▀█")
print(" █▄▄ █▀█ █▀█ ░█░  █░▀░█ ██▄ █▄▀ █ █▄▄ █▄█")
print(" ░░░ ░░░ ░░░ ░░░  ░░░░░ ░░░ ░░░ ░ ░░░ ░░░")
name =  input("¿Cuál es su nombre? ")
print("Por favor",name,"empiece contestando las siguientes preguntas:")

if (input("¿Tiene usted fiebre? ").lower() == 's'):
    Med_kb.tell(expr("Fiebre({})".format(name)))

if (input("¿Tiene usted dolor de garganta? ").lower() == 's'):
    Med_kb.tell(expr("DolorGarganta({})".format(name)))

if (input("¿Tiene usted inflamación en los bronquios? ").lower() == 's'):
    Med_kb.tell(expr("Bronquitis({})".format(name)))

if (input("¿Tiene usted inflamación en los sacos aéreos? ").lower() == 's'):
    Med_kb.tell(expr("Neumonia({})".format(name)))

if (input("¿Tiene usted ojo rosado? ").lower() == 's'):
    Med_kb.tell(expr("Conjuntivitis({})".format(name)))

if (input("¿Maneja usted la frecuencia cardiaca alta? ").lower() == 's'):
    Med_kb.tell(expr("FrecuenciaCardiacaAlta({})".format(name)))

if (input("¿Presentó usted algún aumento en los glóbulos blancos? ").lower() == 's'):
    Med_kb.tell(expr("GainGlobulosBlancos({})".format(name)))

if (input("¿Presenta usted insuficiencia renal? ").lower() == 's'):
    Med_kb.tell(expr("InsuficienciaRenal({})".format(name)))
    
if (input("¿Usted tiene pérdida de apetito? ").lower() == 's'):
    Med_kb.tell(expr("NoHambre({})".format(name)))

if (input("¿Siente usted su abdomen inflamado? ").lower() == 's'):
    Med_kb.tell(expr("InflamacionAbdominal({})".format(name)))

if (input("¿Ha perdido peso anormalmente durante los últimos días? ").lower() == 's'):
    Med_kb.tell(expr("PerdidaDePeso({})".format(name)))

if (input("¿Ha encontrado pus en sus heces? ").lower() == 's'):
    Med_kb.tell(expr("PusFecal({})".format(name)))

if (input("¿Ha usted tenido calambres en el abdomen? ").lower() == 's'):
    Med_kb.tell(expr("CalambreAbdominal({})".format(name)))

if (input("¿Presenta usted sensibilidad abdominal? ").lower() == 's'):
    Med_kb.tell(expr("SensAbdominal({})".format(name)))

if (input("¿Presenta usted diarrea con sangre? ").lower() == 's'):
    Med_kb.tell(expr("DiarreaSangre({})".format(name)))

if (input("¿Presenta usted cólicos? ").lower() == 's'):
    Med_kb.tell(expr("Colicos({})".format(name)))

if (input("¿Presenta usted escalofríos? ").lower() == 's'):
    Med_kb.tell(expr("Escalofrios({})".format(name)))

        #PREGUNTAS DE JUAN PABLO
if (input("¿Siente usted estreñimiento? ").lower() == 's'):
    Med_kb.tell(expr("Estreñimiento({})".format(name)))

if (input("¿Ha observado sangre en sus heces? ").lower() == 's'):
    Med_kb.tell(expr("SangreFecal({})".format(name)))

if (input("¿Tiene usted diarrea? ").lower() == 's'):
    Med_kb.tell(expr("Diarrea({})".format(name)))

if (input("¿Siente usted algún tipo de masa o bulto debajo de su piel? ").lower() == 's'):
    Med_kb.tell(expr("MasaPiel({})".format(name)))

if (input("¿Siente usted dolor abdominal? ").lower() == 's'):
    Med_kb.tell(expr("DolorAbdominal({})".format(name)))

if (input("¿Siente usted dolor de cabeza? ").lower() == 's'):
    Med_kb.tell(expr("DolorCabeza({})".format(name)))
    
if (input("¿Presenta usted diarrea acuosa? ").lower() == 's'):
    Med_kb.tell(expr("DiarreaAcuosa({})".format(name)))

        #PREGUNTAS DE FRANCELIO
if (input("¿Ha sentido náuseas en los últimos días? ").lower() == 's'):
    Med_kb.tell(expr("Nauseas({})".format(name)))

if (input("¿Ha presentado vómitos en los últimos días? ").lower() == 's'):
    Med_kb.tell(expr("Vomito({})".format(name)))

if (input("¿Ha tenido una sensación dolorosa en la mitad del pecho? ").lower() == 's'):
    Med_kb.tell(expr("SensacionDolorosa({})".format(name)))

if (input("¿Ha tenido una sensación ardiente en la mitad del pecho? ").lower() == 's'):
    Med_kb.tell(expr("SensacionArdiente({})".format(name)))

if (input("¿Ha presentado dolor y calambres en el estómago? ").lower() == 's'):
    Med_kb.tell(expr("DistensionAbdominal({})".format(name))) 

if (input("¿Sus heces tienden a ser blandas? ").lower() == 's'):
    Med_kb.tell(expr("HecesBlandas({})".format(name)))

if (input("¿Sus heces tienden a ser grasosas? ").lower() == 's'):
    Med_kb.tell(expr("HecesGrasosas({})".format(name)))

if (input("¿Sus heces tienden a ser voluminosas ? ").lower() == 's'):
    Med_kb.tell(expr("HecesVoluminosas({})".format(name)))

if (input("¿Sus heces tienden a ser heces con mal olor? ").lower() == 's'):
    Med_kb.tell(expr("HecesMalOlor({})".format(name)))

        #PREGUNTAS DE MICHEL
if (input("¿Siente usted dolor muscular intestinal? ").lower() == 's'):
    Med_kb.tell(expr("Dolor({})".format(name))) 

if (input("¿Siente usted la sensación de tener ganas de vomitar? ").lower() == 's'):
    Med_kb.tell(expr("Vomito({})".format(name))) 

if (input("¿Sus heces tienen un color poco natural? ").lower() == 's'):
    Med_kb.tell(expr("HecesClaras({})".format(name))) 

if (input("¿Tiene usted más fatiga de lo normal?").lower() == 's'):
    Med_kb.tell(expr("Fatiga({}) ".format(name))) 

if (input("¿Tiene usted dolor articular?").lower() == 's'):
    Med_kb.tell(expr("Dolor({})".format(name))) 


if (input("¿Presenta usted anemia?").lower() == 's'):
    Med_kb.tell(expr("Anemia({})".format(name))) 

while True:
    print("\nSeleccione una opción:")
    print("1. Diagnósticos")
    print("2. Tratamiento")
    print("3. Salir del menú")

    opcion = input("Opción seleccionada: ")

    if opcion == "1":
        print("Ha seleccionado Diagnósticos")
        # Aquí puedes agregar la lógica para el diagnóstico
        print("\nTu diagnóstico es: ")
        answer = fol_fc_ask(Med_kb, expr("Enfermo({}, x)".format(name)))
        answer = list(answer)

        if len(answer)>0:
            for diag in answer:
                print(diag[x])
        else:
            print("No hay diagnostico")

    elif opcion == "2":
        print("Ha seleccionado Tratamiento")
        # Aquí puedes agregar la lógica para el tratamiento
        print("\nTu tratamiento es: ")
        answer = fol_fc_ask(Med_kb, expr("Tratamiento(x, {})".format(name)))
        answer = list(answer)

        if len(answer)>0:
            for diag in answer:
                print(diag[x])
        else:
            print("No hay tratamientos")

    elif opcion == "3":
        print("Saliendo del menú...")
        break

    else:
        print("Opción inválida, seleccione una opción del menú")

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------