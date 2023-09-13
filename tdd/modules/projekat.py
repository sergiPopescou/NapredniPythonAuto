from tdd.modules.issue import Issue


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        if len(args) > 0:
            instances[class_].naziv = args[0]
        elif "naziv" in kwargs:
            instances[class_].naziv = kwargs["naziv"]
        return instances[class_]

    return get_instance


@singleton
class Projekat:
    """
    Projekat je skup issuea,
    nad njim imaju kontgrolu Vodja projekta i Klijent
    Attributes:
        - naziv - string naziv projekta
        - issues - lista issuea na projektu
    """
    def __init__(self, naziv=None):
        if naziv is None:
            naziv = "PROJEKAT"
        self.naziv = naziv
        self.issues = []

    def __str__(self):
        """
        Stringovna reprezentacija Projekta u formatu [NAZIV]
        :return: string
        """
        return f"[{self.naziv}]"

    def addIssue(self, issue_):
        """
        Funkcija koja dodaje issue.

        :param issue:
        """
        if not isinstance(issue_, Issue):
            raise TypeError("issue needs to be the type of Issue")
        # if issue_.naziv in [i.naziv for i in self.issues]:
        #     raise ValueError("issue needs to have unique name")
        for i in self.issues:
            if i.naziv == issue_.naziv:
                raise ValueError("issue needs to have unique name")
        # time.sleep(randint(1,2))
        self.issues.append(issue_)

    def filterIssuesByNivo(self, nivo):
        """
        Iterator issua projekta odgovarajuceg nivoa

        :param nivo: filter nivo
        :return: iterator issuea
        """
        for i in self.issues:
            if i.checkNivo(nivo):
                yield i

    def getOsobeOnProjekt(self):
        """
        sve osobe na projektu
        :return:
        """
        return set([i.osoba for i in self.issues if i.osoba is not None])
        # maybe add klijent and vodja projekta (ako vec nema na issueu)

    def removeIssueNamed(self, issueName):
        for index_, issue_ in enumerate(self.issues):
            if issue_.naziv == issueName:
                del self.issues[index_]
                return
        return

    def getIssueNamed(self, issueName):
        lst = [i for i in self.issues if i.naziv == issueName]
        if len(lst) == 0:
            return None
        return lst[0]
